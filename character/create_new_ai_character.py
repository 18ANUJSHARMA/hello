import os
import background_text
import csv_text

def create_new_ai_character(character_name):
  """Creates a new AI character with a data folder that contains the file types specified in the prompt.

  Args:
    character_name: The name of the new AI character.
  """

  # Check if the character folder already exists.
  character_folder = os.path.join("character_catalog", character_name)
  if os.path.exists(character_folder):
    raise FileExistsError(f"The character folder '{character_folder}' already exists.")

  # Check if the character name is valid.
  if not character_name or any(not (c.isalnum() or '_')  for c in character_name):
    raise ValueError("The character name must be non-empty and contain only alphanumeric characters.")

  # Create the character folder.
  os.makedirs(character_folder, exist_ok=True)

  # Create the data folder.
  data_folder = os.path.join(character_folder, "data")
  os.makedirs(data_folder, exist_ok=True)

  # Create the files in the data folder. / METHODS TO CREATE DIFFERENTS FILES
  '''for file_type in ["txt", "pdf", "docx", "pptx", "png", "csv", "epub", "md", "mbox", "ipynb"]:
    file_path = os.path.join(data_folder, f"background.{file_type}") 
    with open(file_path, "w") as f:
      f.write(f"This is an example file of type {file_type}.")'''
  
  
  response=background_text.background_character_prompt(character_name)
  print(response)

  file_path = os.path.join(data_folder, f"background.{'txt'}")  # for background file
  with open(file_path, "w") as f:
    #  f.write(f"This is an example file of type {'txt'}.")     
       f.write(response)

  response2=csv_text.csv_character_prompt(character_name)
  file_path = os.path.join(data_folder, f"talk.{'csv'}")   # for csv file
  with open(file_path, "w") as f:
      #f.write(f"This is an example file of type {'csv'}.")
      f.write(response2)


  # Update the `system` file to define the new character.
  system_file = os.path.join(character_folder, "system")  # for system file
  with open(system_file, "w") as f:                         
    f.write("# Character system file\n")
    f.write(f"character_name: {character_name}\n")
   # f.write(f"data_folder: {data_folder}\n")

  print(f"New AI character {character_name} has been created successfully!")


if __name__ == "__main__":
  character_name = input("Enter the name of the new AI character: ")
  create_new_ai_character(character_name)
