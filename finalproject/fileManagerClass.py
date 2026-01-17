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

import os, shutil, glob

extensions = {
    # Images
    ".bmp": "BMP_Images", ".gif": "GIF_Images", ".heic": "HEIC_Images",
    ".jpeg": "JPEG_Images", ".jpg": "JPG_Images", ".png": "PNG_Images",
    ".tiff": "TIFF_Images", ".webp": "WEBP_Images",

    # Videos
    ".avi": "AVI_Videos", ".mkv": "MKV_Videos", ".mov": "MOV_Videos",
    ".mp4": "MP4_Videos", ".mpeg": "MPEG_Videos", ".wmv": "WMV_Videos",

    # Audio
    ".aac": "AAC_Audio", ".flac": "FLAC_Audio", ".mp3": "MP3_Audio",
    ".ogg": "OGG_Audio", ".wav": "WAV_Audio", ".wma": "WMA_Audio",

    # Documents
    ".doc": "DOC_Documents", ".docx": "DOCX_Documents", ".pdf": "PDF_Documents",
    ".ppt": "PPT_Documents", ".pptx": "PPTX_Documents", ".txt": "TXT_Documents",
    ".xls": "XLS_Documents", ".xlsx": "XLSX_Documents",

    # Compressed Files
    ".7z": "7Z_Compressed", ".bz2": "BZ2_Compressed", ".gz": "GZ_Compressed",
    ".rar": "RAR_Compressed", ".tar": "TAR_Compressed", ".zip": "ZIP_Compressed",

    # Programming/Code Files
    ".c": "C_Code", ".cpp": "CPP_Code", ".cs": "CS_Code", ".html": "HTML_Code",
    ".java": "JAVA_Code", ".js": "JS_Code", ".json": "JSON_Files",
    ".php": "PHP_Code", ".py": "PY_Code", ".rb": "RB_Code", ".xml": "XML_Files",

    # Executables
    ".exe": "EXE_Files", ".msi": "MSI_Files", ".sh": "SH_Scripts", ".bat": "BAT_Scripts",

    # Miscellaneous
    ".csv": "CSV_Files", ".ics": "ICS_Calendar", ".md": "Markdown_Files",
    ".rtf": "RTF_Documents", ".sqlite": "SQLite_Databases", ".yml": "YAML_Files"
}

categories = {
    "Images": [".bmp", ".gif", ".heic", ".jpeg", ".jpg", ".png", ".tiff", ".webp"],
    "Videos": [".avi", ".mkv", ".mov", ".mp4", ".mpeg", ".wmv"],
    "Audio": [".aac", ".flac", ".mp3", ".ogg", ".wav", ".wma"],
    "Documents": [".doc", ".docx", ".pdf", ".ppt", ".pptx", ".txt", ".xls", ".xlsx"],
    "Compressed": [".7z", ".bz2", ".gz", ".rar", ".tar", ".zip"],
    "Programming": [".c", ".cpp", ".cs", ".html", ".java", ".js", ".json", ".php", ".py", ".rb", ".xml"],
    "Executable": [".exe", ".msi", ".sh", ".bat"],
    "Miscellaneous": [".csv", ".ics", ".md", ".rtf", ".sqlite", ".yml"]
}

class FileManager:

    def ensure_new_folder(self, dest, folder_name):
        newFolderPath = os.path.join(dest, folder_name)
        os.makedirs(newFolderPath, exist_ok=True)
        return newFolderPath

    def copy_files(self, src, dest, ext_list, folder_name=None):
        if folder_name:
            dest = self.ensure_new_folder(dest, folder_name)

        for file in os.listdir(src):
            filePath = os.path.join(src, file)

            if os.path.splitext(file)[1] in ext_list:
                destPath = os.path.join(dest, file)
                shutil.copy(filePath, destPath)
                print(f"Copied '{file}' to '{dest}'.")
        return dest

    def sort_files(self, src, dest, ext_list, folder_name=None):
        for file in os.listdir(src):
            filePath = os.path.join(src, file)
            fileExt = os.path.splitext(file)[1]

            if fileExt in ext_list:
                subfolderName = extensions.get(fileExt, "Other_Files")
                folderPath = os.path.join(dest, subfolderName)
                os.makedirs(folderPath, exist_ok=True)
                destPath = os.path.join(folderPath, file)
                shutil.move(filePath, destPath)
                print(f"Moved '{file}' to '{folderPath}'.")

    def rename_files(self, src, ext_list, prefix):
        for ext in ext_list:
            files = glob.glob(os.path.join(src, f"*{ext}"))
            files.sort(key=os.path.getctime)

            for index, file_path in enumerate(files):
                newName = f"{prefix}_{str(index + 1).zfill(3)}{ext}"
                destPath = os.path.join(src, newName)
                os.rename(file_path, destPath)
                print(f"Renamed '{file_path}' to '{newName}'.")
