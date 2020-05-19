import pygame

pygame.init()

screen = pygame.display.set_mode()
screen.fill((255, 255, 255))
font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

array_size = int(input('Array size: '))
array = []
for index in range(array_size):
    array_value = int(input('Enter element {}: '.format(index)))
    array.append(array_value)

#graphical representation of array cells
def box(array, highlight_position=None):
    box_position = (30, 200)
    box_size = (50, 50)
    normal_color = (0, 0, 255) 
    highlight_color = (255, 0, 0)#used to highlight search element
    
    screen.fill((255, 255, 255))
    
    for index, item in enumerate(array):
        color = highlight_color if index == highlight_position else normal_color



        pygame.draw.rect(screen, color, box_position + box_size, 2)
        text = font.render(str(index), True, (0, 0, 0))
        screen.blit(text, box_position)


        text = font.render(str(item), True, (0, 0, 0))
        screen.blit(text, tuple(box_position[i] + box_size[i] * 0.4 for i in range(2)))
        box_position = (box_position[0] + int(box_size[0] * 1.05), box_position[1])
    pygame.display.update()    

def search():
    search_element = int(input('Enter search element: '))
    search_index = array.index(search_element) if search_element in array else None
    box(array, highlight_position=search_index)

def sort_array():
    array.sort()
    box(array)

box(array)

pygame.display.update()

input('Press Enter to search for an element')

search()

pygame.display.update()

input('Press Enter to sort the array')

sort_array()

pygame.display.update()

input('Press enter to exit')

pygame.display.quit()
