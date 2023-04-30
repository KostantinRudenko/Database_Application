# Database parameters

DATATYPES = {'integer' : 'INT',
             'boolean' : 'BOOL',
             'varchar' : 'VARCHAR',
             'char'    : 'CHAR'}

KEYS = {'primary_key'  : 'PRIMARY KEY',
        'foreign_key'  : 'FOREIGN KEY'}

OBJECTS = {'database' : 'DATABASE',
           'table' : 'TABLE',
           'index' : 'INDEX'}

# UI Parameters
MAIN_WINDOW_WIDTH = 200
MAIN_WINDOW_HEIGHT = 300

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BUTTON_WIDTH = 10
BUTTON_HEIGHT = 2

LABEL_WIDTH = 30
LABEL_HEIGHT = 1

ENTRY_WIDTH = 30
ENTRY_HEIGHT = 1

TEXT_WIDTH = 40
TEXT_HEIGHT = 20

SIMPLE_MODE_TEXT_WIDTH = 20
SIMPLE_MODE_TEXT_HEIGHT = 10

RESIZABLE_WIDTH = False
RESIZABLE_HEIGHT = False

TITLE = 'Database Application V.1.0.0'

# Regular expression values
REGEX_QUERY = r'[A-Za-z0-9\w\s|*]+;'
TABLE_NAME_QUERY=r'TABLE|table|Table [A-Za-z0-9]+'

# Other values
BROWSERS = ['chrome', 'firefox', 'opera', 'safari']
HELP_LINK = 'https://github.com/Sralker731/Database_Application/wiki' 