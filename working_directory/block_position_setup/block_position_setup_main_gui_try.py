#------------------------------------ SETUP ----------------------------------------------
import sys

WORKING_DIRECTORY = ''
SPLITTING_CHARACTER = ''
if sys.platform.startswith('win') : 
	SPLITTING_CHARACTER = '\{}'.format('')
elif sys.platform.startswith('darwin') : 
	SPLITTING_CHARACTER = '/'

def setup() : 

	def locate_working_directory() : 
		working_directory = ''
		for element in __file__.split(SPLITTING_CHARACTER)[:-2] :
			working_directory += element + '{}'.format(SPLITTING_CHARACTER)
		return working_directory
	
	global WORKING_DIRECTORY
	WORKING_DIRECTORY = locate_working_directory()
	print('working_directory --> ',WORKING_DIRECTORY)
	sys.path.append(WORKING_DIRECTORY)

setup()
#---------------------- TKINTER RELATED FUNCTIONS ---------------------------------------------

from main_directory.gui import gui_maker

main_window = gui_maker.variable_displayer_maker("block_position_setup_variables.txt",mode = "instance_mode")
main_window.mainloop_enable()