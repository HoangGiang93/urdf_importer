#!/usr/bin/python3

bl_info = {
    "name": "Import URDF format",
    "author": "Giang Nguyen",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "category": "Import-Export"
}

# fmt: off
import bpy

from .urdf_importer import URDFImporter
from .urdf_importer import FBXExporter
# fmt: on


def import_menu_func(self, context):
    self.layout.operator(URDFImporter.bl_idname, text="URDF (.urdf)")


def export_menu_func(self, context):
    self.layout.operator(FBXExporter.bl_idname,
                         text="FBX with textures (.fbx)")


def register():
    bpy.utils.register_class(URDFImporter)
    bpy.types.TOPBAR_MT_file_import.append(import_menu_func)
    bpy.utils.register_class(FBXExporter)
    bpy.types.TOPBAR_MT_file_export.append(export_menu_func)


def unregister():
    bpy.utils.unregister_class(URDFImporter)
    bpy.types.TOPBAR_MT_file_import.remove(import_menu_func)
    bpy.utils.unregister_class(FBXExporter)
    bpy.types.TOPBAR_MT_file_export.remove(export_menu_func)
    from os.path import exists
    from shutil import rmtree

    from .urdf_importer import TMP_FOLDER_PATH
    if exists(TMP_FOLDER_PATH):
        rmtree(TMP_FOLDER_PATH)
