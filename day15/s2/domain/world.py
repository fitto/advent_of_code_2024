import copy
from dataclasses import dataclass, field
from typing import List, Tuple, Optional, Set

from day15.s2.domain.big_box import BigBox
from day15.s2.domain.coordinates import Coordinates
from day15.s2.domain.nothing import Nothing
from day15.s2.domain.robot import Robot
from day15.s2.domain.wall import Wall
from day15.s2.domain.world_object import WorldObject


# noinspection PyUnresolvedReferences
@dataclass(frozen=True)
class World:
    robot_position: Coordinates
    places_as_table: List[List[WorldObject]]
    seen_coordinates: Set = field(default_factory=set, init=False)

    @property
    def walls_count(self) -> int:
        all_obj = set()

        for ii in range(self.height()):
            for jj in range(self.width()):
                found_object = self.places_as_table[ii][jj]
                if isinstance(found_object, Wall):
                    all_obj.add(found_object)
        return len(all_obj)

    @property
    def big_boxes_count(self) -> int:
        all_obj = set()

        for ii in range(self.height()):
            for jj in range(self.width()):
                found_object = self.places_as_table[ii][jj]
                if isinstance(found_object, BigBox):
                    all_obj.add(found_object)
        return len(all_obj)

    def width(self, row: int = 0) -> int:
        return len(self.places_as_table[row])

    def height(self) -> int:
        return len(self.places_as_table)

    def object_at(self,
                  coordinates: Coordinates
                  ) -> WorldObject:
        return self.places_as_table[coordinates.first][coordinates.second]

    def move_objects(self,
                     objects_list: List[WorldObject],
                     direction: Tuple
                     ) -> 'World':
        # new_places_as_table = copy.deepcopy(self.places_as_table)
        new_places_as_table = self.places_as_table
        new_objects_list = copy.deepcopy(objects_list)

        for obj in new_objects_list:
            if not isinstance(obj, BigBox):
                print(f' sth is wrong  {obj}')

            # /purge old
            new_places_as_table[obj.current_coordinates_1.first][
                obj.current_coordinates_1.second] = Nothing(
                obj.current_coordinates_1
            )
            new_places_as_table[obj.current_coordinates_2.first][
                obj.current_coordinates_2.second] = Nothing(
                obj.current_coordinates_2
            )

        # print(f' to be moved: {new_objects_list}')
        while len(new_objects_list) > 0:
            old_box = new_objects_list.pop(-1)
            if isinstance(old_box, BigBox):
                new_box = old_box.moved(direction)
                # print(f' to  {new_box.__repr__()}')

                # # /purge old
                # new_places_as_table[old_box.current_coordinates_1.first][
                #     old_box.current_coordinates_1.second] = Nothing(
                #     old_box.current_coordinates_1
                # )
                # new_places_as_table[old_box.current_coordinates_2.first][
                #     old_box.current_coordinates_2.second] = Nothing(
                #     old_box.current_coordinates_2
                # )

                # move to new
                new_places_as_table[new_box.current_coordinates_1.first][
                    new_box.current_coordinates_1.second] = new_box
                new_places_as_table[new_box.current_coordinates_2.first][
                    new_box.current_coordinates_2.second] = new_box

            else:
                print(f' found sth that this not a Box to be moved {old_box}')

        this_robot_current_pos = self.object_at(self.robot_position)
        if not isinstance(this_robot_current_pos, Robot):
            print(f' not found robot where it should be {this_robot_current_pos}')
            self.visualize()
        new_robot = this_robot_current_pos.moved(direction)

        new_places_as_table[self.robot_position.first][self.robot_position.second] = Nothing(
            self.robot_position)
        new_places_as_table[new_robot.current_coordinates.first][
            new_robot.current_coordinates.second] = new_robot

        new_world = World(new_robot.current_coordinates, new_places_as_table)

        return new_world

    def execute_move(self, move: str) -> 'World':
        command_switch = {
            "<": (0, -1),
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0)
        }
        tpl = command_switch[move]

        current_robot = self.object_at(self.robot_position)

        if not isinstance(current_robot, Robot):
            self.visualize()
            print('    did not find robot where it was supposed to be')

        # if isinstance(self.object_at(current_robot.current_coordinates.shifted_coordinates(tpl[0], tpl[1])), Nothing):
        #     return self.move_objects([], tpl)

        list_of_moving_obj = self.list_of_all_moving_objects(
            current_robot.current_coordinates.shifted_coordinates(tpl[0], tpl[1]),
            tpl
        )

        if list_of_moving_obj is None:
            return World(current_robot.current_coordinates, self.places_as_table)
        else:
            return self.move_objects(list_of_moving_obj, tpl)

    def list_of_all_moving_objects(self,
                                   coordinates_to_be_checked: Coordinates,
                                   move_direction: Tuple,
                                   ) -> Optional[List[WorldObject]]:
        moved_objects = set()

        coord_list_to_be_checked = [coordinates_to_be_checked]
        seen_coord = set()

        while len(coord_list_to_be_checked) > 0:
            this_coord = coord_list_to_be_checked.pop()
            this_obj = self.object_at(this_coord)

            if isinstance(this_obj, Wall):
                return None
            elif isinstance(this_obj, BigBox):
                moved_objects.add(this_obj)

                coord1 = this_obj.current_coordinates_1.shifted_coordinates(move_direction[0],
                                                                            move_direction[1])

                coord2 = this_obj.current_coordinates_2.shifted_coordinates(move_direction[0],
                                                                            move_direction[1])

                if move_direction[0] != 0:
                    if coord1 not in seen_coord:
                        coord_list_to_be_checked.append(coord1)
                    if coord2 not in seen_coord:
                        coord_list_to_be_checked.append(coord2)

                else:
                    if move_direction[1] == -1:
                        new_coordinates = coord1
                    else:
                        new_coordinates = coord2

                    if new_coordinates not in seen_coord:
                        coord_list_to_be_checked.append(new_coordinates)

            seen_coord.add(this_coord)

        output = []
        for x in moved_objects:
            if not isinstance(x, BigBox):
                print(f' encountered {x}')
            else:
                output.append(x)

        return output

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
        all_big_boxes = set()

        for ii in range(self.height()):
            for jj in range(self.width()):
                found_object = self.places_as_table[ii][jj]
                if isinstance(found_object, BigBox):
                    all_big_boxes.add(found_object.current_coordinates_1)

        return sum([x.coord_value for x in all_big_boxes])
