from dataclasses import dataclass
from typing import List, Tuple, Optional

from day15.s2.domain.big_box import BigBox
from day15.s2.domain.coordinates import Coordinates
from day15.s2.domain.nothing import Nothing
from day15.s2.domain.robot import Robot
from day15.s2.domain.wall import Wall
from day15.s2.domain.world_object import WorldObject


@dataclass(frozen=True)
class World:
    robot_position: Coordinates
    places_as_table: List[List[WorldObject]]

    def width(self, row: int = 0):
        return len(self.places_as_table[row])

    def height(self):
        return len(self.places_as_table)

    def has_coordinates(self, coordinates: Coordinates) -> bool:
        x1 = coordinates.first
        x2 = coordinates.second

        return -1 < x1 < self.height() and -1 < x2 < self.width()

    def object_at(self, coordinates: Coordinates):
        return self.places_as_table[coordinates.first][coordinates.second]

    def move_objects(self, objects_list: List[WorldObject], direction: Tuple) -> 'World':
        new_places_as_table_copy = self.places_as_table.copy()

        moving_object = objects_list.pop(-1)
        if not isinstance(moving_object, Nothing):
            print('ALARMO !!!!!!!!!!!')

        while len(objects_list) > 1:
            moving_object = objects_list.pop(-1)
            new_obj = moving_object.moved(direction)

            new_places_as_table_copy[new_obj.current_coordinates_1.first][
                new_obj.current_coordinates_1.second] = new_obj
            new_places_as_table_copy[new_obj.current_coordinates_2.first][
                new_obj.current_coordinates_2.second] = new_obj

        moving_object = objects_list.pop(-1)
        if not isinstance(moving_object, Robot):
            print('ALARMO !!!!!! !!!!!! !!!!!')
        new_robot = moving_object.moved(direction)

        new_places_as_table_copy[new_robot.current_coordinates.first][new_robot.current_coordinates.second] = new_robot

        new_places_as_table_copy[moving_object.current_coordinates.first][
            moving_object.current_coordinates.second] = Nothing(
            moving_object.current_coordinates)

        return World(new_robot.current_coordinates, new_places_as_table_copy)

    def robot_move(self, move: str) -> 'World':
        command_switch = {
            "<": (0, -1),
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0)
        }
        tpl = command_switch[move]

        moving_objects = [self.object_at(self.robot_position)]
        if not isinstance(moving_objects[-1], Robot):
            print('ALARMO')

        new_coord = moving_objects[-1]
        while True:
            new_coord = new_coord.current_coordinates.shifted_coordinates(tpl[0], tpl[1])
            found_object = self.object_at(new_coord)
            # print(f'    {found_object}')

            if isinstance(found_object, Nothing):
                moving_objects.append(found_object)
                return self.move_objects(moving_objects, tpl)
            if isinstance(found_object, BigBox):
                if found_object not in moving_objects:
                    moving_obj_list = self.moving_objcts_by_big_box(found_object, tpl, [found_object])
                    if moving_obj_list is None:
                        return self
                    else:
                        for x in moving_obj_list:
                            if x not in moving_objects:
                                moving_objects.append(x)

                        self.move_objects(moving_objects, tpl)
                else:
                    new_coord = new_coord.current_coordinates.shifted_coordinates(tpl[0], tpl[1])

            if isinstance(found_object, Wall):
                return self
            else:
                print('WEIRD')
                print(found_object)

    def moving_objects(self, world_object: WorldObject, move: Tuple, moving_objects_list: List[WorldObject]) -> \
            Optional[List[WorldObject]]:
        if isinstance(world_object, Wall):
            return None
        elif isinstance(world_object, BigBox):
            return self.moving_objcts_by_big_box(world_object, move, moving_objects_list)
        elif isinstance(world_object, Nothing):
            moving_objects_list.append(world_object)
            return moving_objects_list

    def moving_objcts_by_big_box(self, big_box: BigBox, move: Tuple, moving_objects_list: List[WorldObject]) -> \
            Optional[List[WorldObject]]:
        moving_objects_list = [x for x in moving_objects_list]

        if move[0] != 0:
            new_big_box = big_box.moved(move)

            coord1 = new_big_box.current_coordinates_1
            m1 = self.moving_objects(self.object_at(coord1), move, moving_objects_list)
            if m1 is None:
                return None

            coord2 = new_big_box.current_coordinates_2
            m2 = self.moving_objects(self.object_at(coord2), move, moving_objects_list)
            if m2 is None:
                return None

            for x in m1:
                if x not in moving_objects_list:
                    moving_objects_list.append(x)

            for y in m2:
                if y not in moving_objects_list:
                    moving_objects_list.append(y)

            return list(moving_objects_list)

        if move[1] == -1:
            new_obj_at_coordinates = self.object_at(big_box.current_coordinates_1.shifted_coordinates(move[0], move[1]))
        else:
            new_obj_at_coordinates = self.object_at(big_box.current_coordinates_2.shifted_coordinates(move[0], move[1]))

        moving_objects_list.append(big_box)

        return self.moving_objects(
            new_obj_at_coordinates,
            move,
            moving_objects_list
        )

    @staticmethod
    def from_list(this_list: List[List[str]]):
        output = []
        robots_position = ()

        last_added_big_box = None

        for i in range(len(this_list)):
            line = []
            for j in range(len(this_list[i])):
                obj = WorldObject.from_i_j(i, j, this_list[i][j])
                if isinstance(obj, Robot):
                    robots_position = obj.current_coordinates
                if isinstance(obj, BigBox):
                    last_added_big_box = obj
                if obj is None:
                    line.append(last_added_big_box)
                else:
                    line.append(obj)
            output.append(line)

        return World(robots_position, output)

    def visualize(self):
        for ii in range(self.height()):
            this_line = ''

            jj = 0
            while jj < self.width():
                found_object = self.places_as_table[ii][jj]
                this_line += found_object.__str__()
                if isinstance(found_object, BigBox):
                    jj += 2
                else:
                    jj += 1

            print(this_line)

    @property
    def all_coordinates_value(self) -> int:
        output = 0
        for ii in range(self.width()):
            for jj in range(self.height()):
                found_object = self.places_as_table[ii][jj]
                if isinstance(found_object, BigBox):
                    output += found_object.current_coordinates.coord_value

        return output
