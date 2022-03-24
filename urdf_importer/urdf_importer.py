#!/usr/bin/python3

import bpy
from bpy_extras.io_utils import ImportHelper

from .robot_builder import RobotBuilder


def read_data(filepath):
    RobotBuilder(filepath)

    return {'FINISHED'}


class URDFImporter(bpy.types.Operator, ImportHelper):
    """Load a URDF file"""
    bl_idname = "import_scene.urdf"
    bl_label = "Import URDF"

    # ImportHelper mixin class uses this
    filename_ext = ".urdf"

    def execute(self, _):
        return read_data(self.filepath)
