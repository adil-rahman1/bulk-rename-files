import os

directory = input('Enter the name of the directory that contains the files to be renamed: ')
company_initials = input('Enter the company initials: ')

def main():

  for filename in os.listdir(directory):
    format_date(filename)

  for filename in os.listdir(directory):
    add_company_initials(filename)


def format_date(filename):
  day = filename[8:10]
  src = f"{directory}/{filename}"
  if not day.isnumeric():
    date = filename[:7]
    rest_of_filename = filename[8:]
    new_file_name = f"{date}.01_{rest_of_filename}"
    dst = f"{directory}/{new_file_name[2:]}"
  else:
    dst = f"{directory}/{filename[2:]}"
  os.rename(src, dst)
  

def add_company_initials(filename):
  src = f"{directory}/{filename}"
  date = filename[:8]
  rest_of_filename = filename[9:]
  dst = f"{directory}/{date}_{company_initials}_{rest_of_filename}"
  os.rename(src, dst)

if __name__ == '__main__':
  main()