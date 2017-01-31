from bs4 import BeautifulSoup

def find_tags(input_tag , input_attr , input_attr_value):
    try:
        soup = BeautifulSoup(open('sampleHTML1.html'))
        tag = soup.find(input_tag , {input_attr : input_attr_value})
        print(tag.string)
    except AttributeError:
        print('No such attribute/tag/value')
    except Exception:
        print('Some error occoured')

input_tag = raw_input('Enter a tag to find in file\n')
input_attr = raw_input('Enter a attribute to find in file\n')
input_attr_value = raw_input('Enter the attribute value to find in file\n')
find_tags(input_tag , input_attr , input_attr_value)