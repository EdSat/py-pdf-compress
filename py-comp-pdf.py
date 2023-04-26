import os

input_folder = "input_folder/"
output_folder = "output_folder/"

for file_name in os.listdir(input_folder):
    if file_name.endswith(".pdf"):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)
        cmd = f'gswin64c -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile="{output_file_path}" "{input_file_path}"'
        os.system(cmd)

print("Done.")
