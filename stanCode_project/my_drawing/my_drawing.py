"""
File: my_drawing
Name: jessie
----------------------
This file uses the campy to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


window = GWindow(600, 500)


def main():
    """
    Title: Summer time!
    夏天就是要去海邊玩～
    """
    # sky
    sky = GRect(600, 310)
    sky.filled = True
    sky.fill_color = 'lightblue'
    sky.color = 'lightblue'
    window.add(sky, x=0, y=0)

    # sun
    sun = GOval(250, 250)
    sun.filled = True
    sun.fill_color = 'lemon chiffon'
    sun.color = 'lemon chiffon'
    window.add(sun, x=(window.width-sun.width)/2, y=(window.height-sun.height)/2)

    # cloud
    cloud1 = GOval(200, 200)
    cloud1.filled = True
    cloud1.fill_color = 'white'
    cloud1.color = 'white'
    window.add(cloud1, x=30, y=220)

    cloud2 = GOval(250, 250)
    cloud2.filled = True
    cloud2.fill_color = 'white'
    cloud2.color = 'white'
    window.add(cloud2, x=-150, y=150)

    cloud3 = GOval(100, 100)
    cloud3.filled = True
    cloud3.fill_color = 'white'
    cloud3.color = 'white'
    window.add(cloud3, x=180, y=280)

    cloud6 = GOval(300, 300)
    cloud6.filled = True
    cloud6.fill_color = 'white'
    cloud6.color = 'white'
    window.add(cloud6, x=220, y=250)

    cloud4 = GOval(250, 250)
    cloud4.filled = True
    cloud4.fill_color = 'white'
    cloud4.color = 'white'
    window.add(cloud4, x=450, y=180)

    cloud5 = GOval(100, 100)
    cloud5.filled = True
    cloud5.fill_color = 'white'
    cloud5.color = 'white'
    window.add(cloud5, x=550, y=150)

    # sea
    sea = GRect(600, 120)
    sea.filled = True
    sea.fill_color = 'cornflowerblue'
    sea.color = 'cornflowerblue'
    window.add(sea, x=0, y=sky.height)

    # sea2
    sea2 = GOval(2000, 10)
    sea2.filled = True
    sea2.fill_color = 'slateblue'
    sea2.color = 'slateblue'
    window.add(sea2, x=0, y=350)

    sea3 = GOval(2000, 5)
    sea3.filled = True
    sea3.fill_color = 'aliceblue'
    sea3.color = 'aliceblue'
    window.add(sea3, x=-1600, y=380)

    sea4 = GOval(2000, 5)
    sea4.filled = True
    sea4.fill_color = 'royalblue'
    sea4.color = 'royalblue'
    window.add(sea4, x=-1800, y=320)

    sea5 = GOval(2000, 10)
    sea5.filled = True
    sea5.fill_color = 'powderblue'
    sea5.color = 'powderblue'
    window.add(sea5, x=350, y=320)

    # sand
    sand1 = GRect(600, 100)
    sand1.filled = True
    sand1.fill_color = 'wheat'
    sand1.color = 'wheat'
    window.add(sand1, x=0, y=(window.height - sand1.height))

    # seebirb
    bird1 = GArc(30, 30, 350, 180)
    bird1.filled = True
    bird1.fill_color = 'white'
    bird1.color = 'white'
    window.add(bird1, x=30, y=30)

    bird2 = GArc(30, 30, 10, 180)
    bird2.filled = True
    bird2.fill_color = 'white'
    bird2.color = 'white'
    window.add(bird2, x=60, y=30)

    wing1 = GPolygon()
    wing1.add_vertex((30, 36))
    wing1.add_vertex((38, 30))
    wing1.add_vertex((38, 38))
    wing1.filled = True
    window.add(wing1)

    wing2 = GPolygon()
    wing2.add_vertex((90, 36))
    wing2.add_vertex((82, 30))
    wing2.add_vertex((82, 38))
    wing2.filled = True
    window.add(wing2)

    bird3 = GArc(30, 30, 350, 180)
    bird3.filled = True
    bird3.fill_color = 'white'
    bird3.color = 'white'
    window.add(bird3, x=360, y=150)

    bird4 = GArc(30, 30, 10, 180)
    bird4.filled = True
    bird4.fill_color = 'white'
    bird4.color = 'white'
    window.add(bird4, x=390, y=150)

    wing3 = GPolygon()
    wing3.add_vertex((360, 158))
    wing3.add_vertex((368, 152))
    wing3.add_vertex((368, 160))
    wing3.filled = True
    window.add(wing3)

    wing4 = GPolygon()
    wing4.add_vertex((420, 156))
    wing4.add_vertex((412, 150))
    wing4.add_vertex((412, 158))
    wing4.filled = True
    window.add(wing4)

    # boat
    boat1 = GPolygon()
    boat1.add_vertex((100, 280))
    boat1.add_vertex((100, 330))
    boat1.add_vertex((130, 330))
    boat1.filled = True
    window.add(boat1)

    boat2 = GRect(3, 10)
    boat2.filled = True
    window.add(boat2, x=112, y=330)

    boat3 = GOval(30, 10, x=100, y=340)
    boat3.filled = True
    window.add(boat3)

    # board
    board = GOval(100, 500)
    board.filled = True
    board.fill_color = 'lightcoral'
    board.color = 'lightcoral'
    window.add(board, x=450, y=250)

    board2 = GPolygon()
    board2.add_vertex((466, 310))
    board2.add_vertex((529, 300))
    board2.add_vertex((534, 320))
    board2.filled = True
    board2.fill_color = 'white'
    board2.color = 'white'
    window.add(board2)

    board3 = GPolygon()
    board3.add_vertex((545, 410))
    board3.add_vertex((455, 400))
    board3.add_vertex((453, 420))
    board3.filled = True
    board3.fill_color = 'white'
    board3.color = 'white'
    window.add(board3)

    board4 = GPolygon()
    board4.add_vertex((455, 499))
    board4.add_vertex((548, 490))
    board4.add_vertex((548, 510))
    board4.filled = True
    board4.fill_color = 'white'
    board4.color = 'white'
    window.add(board4)

    # blanket
    blanket = GRect(200, 100, x=50, y=430)
    blanket.filled = True
    blanket.fill_color = 'seashell'
    blanket.color = 'seashell'
    window.add(blanket)

    blanket1 = GRect(5, 100, x=60, y=430)
    blanket1.filled = True
    blanket1.fill_color = 'sage'
    blanket1.color = 'sage'
    window.add(blanket1)
    blanket2 = GRect(5, 100, x=77, y=430)
    blanket2.filled = True
    blanket2.fill_color = 'sage'
    blanket2.color = 'sage'
    window.add(blanket2)
    blanket3 = GRect(2, 100, x=70, y=430)
    blanket3.filled = True
    blanket3.fill_color = 'sage'
    blanket3.color = 'sage'
    window.add(blanket3)

    blanket4 = GRect(5, 100, x=110, y=430)
    blanket4.filled = True
    blanket4.fill_color = 'sage'
    blanket4.color = 'sage'
    window.add(blanket4)
    blanket5 = GRect(5, 100, x=127, y=430)
    blanket5.filled = True
    blanket5.fill_color = 'sage'
    blanket5.color = 'sage'
    window.add(blanket5)
    blanket6 = GRect(2, 100, x=120, y=430)
    blanket6.filled = True
    blanket6.fill_color = 'sage'
    blanket6.color = 'sage'
    window.add(blanket6)

    blanket7 = GRect(5, 100, x=160, y=430)
    blanket7.filled = True
    blanket7.fill_color = 'sage'
    blanket7.color = 'sage'
    window.add(blanket7)
    blanket8 = GRect(5, 100, x=177, y=430)
    blanket8.filled = True
    blanket8.fill_color = 'sage'
    blanket8.color = 'sage'
    window.add(blanket8)
    blanket9 = GRect(2, 100, x=170, y=430)
    blanket9.filled = True
    blanket9.fill_color = 'sage'
    blanket9.color = 'sage'
    window.add(blanket9)

    blanket10 = GRect(5, 100, x=210, y=430)
    blanket10.filled = True
    blanket10.fill_color = 'sage'
    blanket10.color = 'sage'
    window.add(blanket10)
    blanket11 = GRect(5, 100, x=227, y=430)
    blanket11.filled = True
    blanket11.fill_color = 'sage'
    blanket11.color = 'sage'
    window.add(blanket11)
    blanket12 = GRect(2, 100, x=220, y=430)
    blanket12.filled = True
    blanket12.fill_color = 'sage'
    blanket12.color = 'sage'
    window.add(blanket12)

    # slipper
    slipper = GOval(15, 25, x=240, y=420)
    slipper.filled = True
    slipper.fill_color = 'darkgrey'
    slipper.color = 'darkgrey'
    window.add(slipper)
    slipper1 = GOval(15, 25, x=258, y=420)
    slipper1.filled = True
    slipper1.fill_color = 'darkgrey'
    slipper1.color = 'darkgrey'
    window.add(slipper1)
    slipper2 = GLine(x0=247, y0=425, x1=240, y1=430)
    slipper2.color = 'white'
    window.add(slipper2)
    slipper3 = GLine(x0=247, y0=425, x1=255, y1=430)
    slipper3.color = 'white'
    window.add(slipper3)
    slipper4 = GLine(x0=265, y0=425, x1=258, y1=430)
    slipper4.color = 'white'
    window.add(slipper4)
    slipper5 = GLine(x0=265, y0=425, x1=272, y1=430)
    slipper5.color = 'white'
    window.add(slipper5)

    summer = GLabel('SUMMER TIME')
    summer.font = 'Courier-60-italic-bold'
    window.add(summer, x=150, y=summer.height+40)


if __name__ == '__main__':
    main()
