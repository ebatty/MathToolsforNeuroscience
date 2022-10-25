# Inspired by Neuromatch generate_book.py https://github.com/NeuromatchAcademy/nmaci
import yaml
import json

def main():

    # Get list of notebooks
    with open('_toc.yml') as fh:
        materials = yaml.load(fh, Loader=yaml.FullLoader)

    notebook_list = []
    for i_part in range(len(materials['parts'])):
        for i_chapter in range(len(materials['parts'][i_part]['chapters'])):
            for i_section in range(len(materials['parts'][i_part]['chapters'][i_chapter]['sections'])):
                notebook_list.append( materials['parts'][i_part]['chapters'][i_chapter]['sections'][i_section]['file'])

    # Process all notebooks
    for notebook_file_path in notebook_list:
        if '.ipynb' in notebook_file_path:
            pre_process_notebook(notebook_file_path)


def pre_process_notebook(file_path):
    print(file_path)
    with open(file_path, encoding="utf-8") as read_notebook:
        content = json.load(read_notebook)

    pre_processed_content = prevent_margin_overlap(content)
    pre_processed_content = link_hidden_cells(pre_processed_content)

    with open(file_path, "w", encoding="utf-8") as write_notebook:
        json.dump(pre_processed_content, write_notebook, indent=1, ensure_ascii=False)


def prevent_margin_overlap(content):

    for cell in content['cells']:
        # Put video in ipywidget so they don't overlap margin
        if len(cell['source']) > 1 and 'YouTubeVideo' in ''.join(cell['source']):
            vid_id =  ''.join(cell['source']).split('"')[1]
            cell['source'] = ['# @markdown\n',
                              'from IPython.display import YouTubeVideo\n',
                              'from ipywidgets import widgets\n',
                              'out = widgets.Output()\n',
                              'with out:\n',
                              f'    display(YouTubeVideo(id=f"{vid_id}", width=730, height=410, fs=1))\n',
                              'display(out)']

        # Put slides in ipywidget so they don't overlap margin
        if len(cell['source']) > 1 and 'IFrame' in cell['source'][1]:
            slide_link = ''.join(cell['source']).split('"')[1].split(", width")[0][:-1]
            cell['source'] = ['# @markdown\n',
                              'from IPython.display import IFrame\n',
                              'from ipywidgets import widgets\n',
                              'out = widgets.Output()\n',
                              'with out:\n',
                              f'    display(IFrame(src=f"{slide_link}", width=730, height=410))\n',
                              'display(out)']
    return content


def link_hidden_cells(content):
    cells = content['cells']
    updated_cells = cells.copy()

    i_updated_cell = 0
    for i_cell, cell in enumerate(cells):
        updated_cell = updated_cells[i_updated_cell]
        if "source" not in cell:
            continue
        if len(cell['source']) == 0:
            continue

        source = cell['source'][0]

        if source.startswith("#") and cell['cell_type'] == 'markdown':
            header_level = source.count('#')
        elif source.startswith("---") and cell['cell_type'] == 'markdown':
            if len(cell['source']) > 1 and cell['source'][1].startswith("#") and cell['cell_type'] == 'markdown':
                header_level = cell['source'][1].count('#')

        if '@title' in source or '@markdown' in source:
            if 'metadata' not in cell:
                updated_cell['metadata'] = {}
            if 'tags' not in cell['metadata']:
                updated_cell['metadata']['tags'] = []

            # Check if cell is video one
            if 'YouTubeVideo' in ''.join(cell['source']) or 'IFrame' in ''.join(cell['source']):
                if "remove-input" not in cell['metadata']['tags']:
                    updated_cell['metadata']['tags'].append("remove-input")
            else:
                if "hide-input" not in cell['metadata']['tags']:
                    updated_cell['metadata']['tags'].append("hide-input")

            # If header is lost, create one in markdown
            if '@title' in source:

                if source.split('@title')[1] != '':
                    header_cell = {
                        'cell_type': 'markdown',
                        'metadata': {},
                        'source': ['#'*(header_level + 1) + ' ' + source.split('@title')[1]]}
                    updated_cells.insert(i_updated_cell, header_cell)
                    i_updated_cell += 1

            strings_with_markdown = [(i, string) for i, string in enumerate(cell['source']) if '@markdown' in string]
            if len(strings_with_markdown) == 1 and 'solution' not in strings_with_markdown[0][1]:
                i = strings_with_markdown[0][0]
                if cell['source'][i].split('@markdown')[1] != '':
                    header_cell = {
                        'cell_type': 'markdown',
                        'metadata': {},
                        'source': [cell['source'][i].split('@markdown')[1]]}
                    updated_cells.insert(i_updated_cell, header_cell)
                    i_updated_cell += 1

        i_updated_cell += 1

    content['cells'] = updated_cells
    return content


if __name__ == '__main__':
    main()
