class Template:
    """
    A template class for handling file-based text templating with tag replacement.

    This class provides functionality to load a template file, replace specified tags
    with content, and optionally write the result to an output file.

    Attributes:
        filename (str): Path to the input template file
        output_filename (str, optional): Path to the output file where the report is written
        content (str): The current content of the template after any replacements
    """
    def __init__(self, filename, output_filename=None):
        self.filename = filename
        self.output_filename = output_filename
        with open(filename, 'r') as f:
            self.content = f.read()

    def replace(self, tag, content):
        self.content = self.content.replace(tag, content)
        if self.output_filename:
            with open(self.output_filename, 'w') as f:
                f.write(self.content)