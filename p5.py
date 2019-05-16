if (command == 'right click'):
	pag.click(button='right')
        elif (command == 'left click'):
            pag.click(button='left')
        elif (command == 'double right click'):
            pag.click(button='right', clicks=2)
        elif (command == 'double left click'):
            pag.click(button='left', clicks=2)
        elif(command == '\n'):
            pag.press('enter')
        elif (command == 'backspace'):
            pag.click(button='left')
            pag.press('backspace')
        elif (command == 'select all'):    '''TO be tested'''
            pag.click(button='left')
            pag.press(['ctrl', 'a'])
        else:
            pag.click(button='left', clicks=3)
            keyb.type_string(command)



