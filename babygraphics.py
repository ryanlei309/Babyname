"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-----------------------
File: babygraphics.py
Name: Ryan Lei
-----------------------
DESCRIPTION: This program add all the baby name files to the name_data
dictionary, and let user able to search the name in case-insensitive way.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # Get the space between the lines.
    line_space = (width - GRAPH_MARGIN_SIZE*2)/len(YEARS)

    # Movement by year_index on x_coordinate.
    x_coordinate = GRAPH_MARGIN_SIZE + (year_index * line_space)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Create the line from the bottom and the top of the window.
    canvas.create_line(0, GRAPH_MARGIN_SIZE, 1000, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, 1000, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # Create the line between the year text.
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, 600, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################

    # Index of the COLORS.
    color_index = 0

    # When user input the name is in name_data, create the line in different year and show the name and rank.
    for name in lookup_names:
        if name in name_data:

            # Pick the color. And the index will plus one in order to pick the next color.
            color = COLORS[color_index]
            color_index += 1

            # Store rank 1000 in the list to store the rank from the data name dictionary.
            data_rank = [str(CANVAS_WIDTH)]*12

            # Loop over the year and rank in name data.
            for i in range(len(YEARS)):

                # Replace rank 1000 to the correct rank if both year appears in dictionary and YEARS.
                if str(YEARS[i]) in name_data[name]:
                    data_rank[i] = name_data[name][str(YEARS[i])]

            # If all the years in the name dictionary appear in YEARS, loop over the year index.
            if len(data_rank) == len(YEARS):
                for j in range(len(YEARS)-1):

                    # Staring point of the line, name and the rank.
                    xn = (get_x_coordinate(CANVAS_WIDTH, j))
                    yn = int((int(data_rank[j]) * int(CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE))/1000) + int(GRAPH_MARGIN_SIZE)

                    # If the rank is out of 1000, show the rank in '*', else, show the correct rank.
                    if yn == (int(CANVAS_HEIGHT) - int(GRAPH_MARGIN_SIZE)):
                        canvas.create_text(xn + TEXT_DX, int(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE),
                                           text=str(name) + ' ' + str('*'), anchor=tkinter.SW, fill=color)

                    else:
                        canvas.create_text(xn + TEXT_DX, yn,
                                           text=str(name) + ' ' + str(data_rank[j]), anchor=tkinter.SW, fill=color)

                    # Next point of the line.
                    xn_1 = (get_x_coordinate(CANVAS_WIDTH, j+1))
                    yn_1 = int((int(data_rank[j+1]) * int(CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)) / 1000) + int(GRAPH_MARGIN_SIZE)

                    # Draw the line, name and the rank.
                    canvas.create_line(xn, yn, xn_1, yn_1, width=LINE_WIDTH, fill=color)

                    # If the rank is out of 1000, show the rank in '*', else, show the correct rank.
                    if yn_1 == (int(CANVAS_HEIGHT) - int(GRAPH_MARGIN_SIZE)):
                        canvas.create_text(xn_1 + TEXT_DX, int(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE),
                                           text=str(name) + ' ' + str('*'), anchor=tkinter.SW, fill=color)

                    else:
                        canvas.create_text(xn_1+TEXT_DX, yn_1,
                                           text=str(name)+' '+str(data_rank[j+1]), anchor=tkinter.SW, fill=color)

            # When all the colors were used, back to the first color in COLORS.
            if color_index == 4:
                color_index = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
