from lxml import etree

def process_xaml(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        xaml_content = file.read()

    root = etree.fromstring(xaml_content)

    color_resources = {}

    def findreplace_colors(element):
        for attr in element.attrib:
            value = element.attrib[attr]

            if value.startswith('#'):
                if value not in color_resources.values():
                    name = f'Color{len(color_resources)}'
                    color_resources[name] = value
                else:
                    name = [key for key, val in color_resources.items() if val == value][0]

                element.attrib[attr] = f'{{StaticResource {name}}}'

            if element.tag.endswith('GradientStop'):
                if value in color_resources.values():
                    name = [key for key, val in color_resources.items() if val == value][0]
                    element.attrib[attr] = f'{{Binding Source={{StaticResource {name}}}, Path=Color}}'

        for child in element:
            findreplace_colors(child)

    findreplace_colors(root)

    resources_str = ""
    for name, color in color_resources.items():
        resources_str += f'    <SolidColorBrush x:Key="{name}" Color="{color}" />\n'

    xaml_str = etree.tostring(root, pretty_print=True, encoding='unicode')
    xaml_str = xaml_str.replace("<Window.Resources>", f"<Window.Resources>\n{resources_str}")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(xaml_str)

input_file = 'markup.xaml'
output_file = 'updated_markup.xaml'

process_xaml(input_file, output_file)
