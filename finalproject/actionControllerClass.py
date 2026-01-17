# FinalProject - A file management application
# Copyright (C) 2024 Samantha Ann Erickson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from finalproject.fileManagerClass import FileManager

class ActionController:
    def __init__(self):
        self.fileManager = FileManager()

    def execute_action(self, action, src, dest, ext_list, prefix, folder_name):
        if action == "Copy Only":
            self.fileManager.copy_files(src, dest, ext_list, folder_name)
            
        elif action == "Rename Only":
            self.fileManager.rename_files(src, ext_list, prefix)

        elif action == "Sort Only":
            self.fileManager.sort_files(src, dest, ext_list, folder_name)
            
        elif action == "Copy & Rename":
            finalDest = self.fileManager.copy_files(src, dest, ext_list, folder_name)
            self.fileManager.rename_files(finalDest, ext_list, prefix)
        
        elif action == "Copy & Sort":
            finalDest = self.fileManager.copy_files(src, dest, ext_list, folder_name)
            self.fileManager.sort_files(finalDest, finalDest, ext_list, None)
        
        elif action == "Rename & Sort":
            self.fileManager.rename_files(src, ext_list, prefix)
            self.fileManager.sort_files(src, dest, ext_list, folder_name)

        elif action == "Copy & Rename & Sort":
            finalDest = self.fileManager.copy_files(src, dest, ext_list, folder_name)
            self.fileManager.rename_files(finalDest, ext_list, prefix)
            self.fileManager.sort_files(finalDest, finalDest, ext_list, None)
