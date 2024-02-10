#!/usr/bin/python3
"""documontation"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
"""import doc"""

class HBNBCommand(cmd.Cmd):
    prompt ="(hbnb)"
    all_class = ["BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"]

    attr_str = ["name", "amenity_id", "place_id", "state_id",
                "user_id", "city_id", "description", "text",
                "email", "password", "first_name", "last_name"]
    attr_int = ["number_rooms", "number_bathrooms",
                "max_guest", "price_by_night"]
    attr_float = ["latitude", "longitude"]

    def do_EOF(self, arg):
        """Cntr + D"""
        print()
        return True

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def empty_line(self):
        """Entre and an empty line-> not execute """
        pass

    def Do_create(self, arg):
        class = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valide_classname:
            print("** class doesn't exist **")
            return

        if self.valid(arg):
            argts = arg.split()
            if argts[0] in class:
                new_inst = class[argts[0]]()
            storage.save()
            print(new_inst.id)

    def Do_show(self, arg):
        """Prints the string representation of an instance"""
        argts = arg.split(' ')
        if not argts:
            print("** class name missing **")
            return

        if self.valid(arg, True):
            argts = arg.split()
            _key = argts[0]+"."+argts[1]
            print(storage.all()[_key])

    def Do_destroy(self, arg):
        if self.valid(arg, True):
            argts = arg.split()
            _key = argts[0]+"."+argts[1]
            del storage.all()[_key]
            storage.save()

    def Do_all(self, arg):
        argts = arg.split()
        _lenght = len(args)
        my_list = []
        if _lenght >= 1:
            if argts[0] not in HBNBCommand.all_class:
                print("** class doesn't exist **")
                return
            for key, val in storage.all().items():
                if argts[0] in key:
                    my_list.append(str(val))
        else:
            for key, val in storage.all().items():
                my_list.append(str(val))
        print(my_list)


    def Do_update(self, arg):

        if not argts:
            print("** class name missing **")
            return

        if self.valid(arg, True, True):
            argts = arg.split()
            _key = argts[0]+"."+argts[1]
            if argts[3].startswith('"'):
                match = re.search(r'"([^"]+)"', arg).group(1)
            elif argts[3].startswith("'"):
                match = re.search(r'\'([^\']+)\'', arg).group(1)
            else:
                match = argts[3]
            if argts[2] in HBNBCommand.attr_str:
                setattr(storage.all()[_key], argts[2], str(match))
            elif argts[2] in HBNBCommand.attr_int:
                setattr(storage.all()[_key], argts[2], int(match))
            elif argts[2] in HBNBCommand.attr_float:
                setattr(storage.all()[_key], argts[2], float(match))
            else:
                setattr(storage.all()[_key], argts[2], self.casting(match))
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
