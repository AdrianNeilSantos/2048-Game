import csv
import operator
from datetime import date
import tkinter as tk
import copy
import random
PlayerName = " "
counterr = 0
#Function for the game + game over screen


def compareScore():
    #read csv and sort
    with open("highscore.csv", "r") as readThis:

        lines = csv.reader(readThis, delimiter=',')
        sort = sorted(lines, key=lambda n: (int(n[1])), reverse=True)

        length = len(sort)
        while(length > 5):
            length -= 1
            sort.pop(length)

    #rewrite all scores based on sorted
    with open("highscore.csv", "w", newline="") as writeHere:
        write = csv.writer(writeHere)
        write.writerows(sort)

def appendNewScore(PLAYERNAME, SCORE):

    getDate = date.today()
    currentDate = getDate.strftime("%b %d %Y")
    # say name and score are initialized
    # for program consider asked name and new score
    with open("highscore.csv", "a+") as appendScore:
        appendScore.write(f"{PLAYERNAME},")
        appendScore.write(f"{SCORE},")
        appendScore.write(f"{currentDate}\n")
    compareScore()

def main_game_window():
    global PlayerName, counterr
    global random_block, Block1, Block2, Block3, Block4, Coor_blocks, root
    global random_block_label, blocklist, counter
    global block_1, block_1_label, block_2, block_2_label, block_3, block_3_label, block_4, block_4_label, block_5, block_5_label, block_6, block_6_label, block_7, block_7_label, block_8, block_8_label, block_9, block_9_label, block_10, block_11_label, block_12, block_12_label, block_13, block_13_label, block_14, block_14_label, block_15, block_15_label, block_16, block_16_label
    global blocks, Blockt1, score, Score_Label_value

    W = 702
    H = 900

    counter = 0
    root = tk.Tk()
    root.maxsize(W,H)
    root.minsize(W,H)
    root.title("2048")
    # HEIGHT(H) and WIDTH(W) of Canvas


    # HEIGHT(h) and WIDTH(w) of the main game border (2048) blocks
    w = 602
    h = 602
    w1 = w - 2
    h1 = (h - 2)

    # Canvas Size
    canvas = tk.Canvas(root, width=W, height=H, bg="#F8F8F0")  # Orig: #F8F8F0
    canvas.pack()

    # Coordinates of blocks
    coor_block1 = [[0, 0], [(w1 // 4), (h1 // 4)]]
    coor_block2 = [[(w1 // 4), 0], [w1 // 2, h1 // 4]]
    coor_block3 = [[(w1 // 2), 0], [3 * w1 // 4, h1 // 4]]
    coor_block4 = [[(3 * w1 // 4), 0], [w1, h1 // 4]]

    coor_block5 = [[0, h1 // 4], [w1 // 4, h1 // 2]]
    coor_block6 = [[w1 // 4, h1 // 4], [w1 // 2, h1 // 2]]
    coor_block7 = [[w1 // 2, h1 // 4], [3 * w1 // 4, h1 // 2]]
    coor_block8 = [[3 * w1 // 4, h1 // 4], [w1, h1 // 2]]

    coor_block9 = [[0, h1 // 2], [w1 // 4, 3 * h1 // 4]]
    coor_block10 = [[w1 // 4, h1 // 2], [w1 // 2, 3 * h1 // 4]]
    coor_block11 = [[w1 // 2, h1 // 2], [3 * w1 // 4, 3 * h1 // 4]]
    coor_block12 = [[3 * w1 // 4, h1 // 2], [w1, 3 * h1 // 4]]

    coor_block13 = [[0, 3 * h1 // 4], [w1 // 4, h1]]
    coor_block14 = [[w1 // 4, 3 * h1 // 4], [w1 // 2, h1]]
    coor_block15 = [[w1 // 2, 3 * h1 // 4], [3 * w1 // 4, h1]]
    coor_block16 = [[3 * w1 // 4, 3 * h1 // 4], [w1, h1]]

    coor_Block1 = [coor_block1, coor_block2, coor_block3, coor_block4]
    coor_Block2 = [coor_block5, coor_block6, coor_block7, coor_block8]
    coor_Block3 = [coor_block9, coor_block10, coor_block11, coor_block12]
    coor_Block4 = [coor_block13, coor_block14, coor_block15, coor_block16]

    coor_blocks = [coor_Block1, coor_Block2, coor_Block3, coor_Block4]
    Coor_blocks = [coor_block1, coor_block2, coor_block3, coor_block4, coor_block5, coor_block6, coor_block7, coor_block8, coor_block9, coor_block10, coor_block11, coor_block12, coor_block13, coor_block14, coor_block15, coor_block16]



    def reposition_coordinates():
        for i in range(len(coor_blocks)):
            for j in coor_blocks:
                j[i][0][0] += 50  # For the Width (x coordinate)
                j[i][0][1] += 250  # For the Height (y coordinate)

                j[i][1][0] += 50  # For the Width (x coordinate)
                j[i][1][1] += 250  # For the Height (y coordinate)


    reposition_coordinates()

    canvas_frame_coor = [[coor_block1[0][0] - 5, coor_block1[0][1] - 5], [coor_block16[1][0] + 5, coor_block16[1][1] + 5]]

    # Game Blocks

    Block1 = [0, 0, 0, 0]
    Block2 = [0, 0, 0, 0]
    Block3 = [0, 0, 0, 0]
    Block4 = [0, 0, 0, 0]
    def restart():
        root.destroy()
        main_game_window()



    blocks = [Block1, Block2, Block3, Block4]
    Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]


    # For randomizing numbers (used in spawning random number)
    inducerlist = [0, 1, 2, 3]
    randomlist = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]

    score = 0

    # Block attributes (color colors in hexadecimal value):
    attribute_0 = ['#CCC0B2', '#786E64']
    attribute_2 = ['#EEE4DA', '#786E64']
    attribute_4 = ['#ECE0CA', '#7A6F6D']
    attribute_8 = ['#F5B174', '#FFECD5']
    attribute_16 = ['#F29762', '#F9F8F0']
    attribute_32 = ['#F17C5A', '#FEF0E6']
    attribute_64 = ['#F75D3B', '#FFF3DC']
    attribute_128 = ['#EFCE71', '#FDF7F1']
    attribute_256 = ['#ECCC65', '#FBF0EB']
    attribute_512 = ['#F0C64E', '#FFF5E3']
    attribute_1024 = ['#EBC544', '#FCFBEB']
    attribute_2048 = ['#ECC135', '#FFFDD8']
    attribute_4096 = ['#3E3A31', '#EEE4DA']
    attributes = [attribute_0, attribute_2, attribute_4, attribute_8, attribute_16, attribute_32, attribute_64, attribute_128, attribute_128, attribute_256, attribute_512, attribute_1024, attribute_2048]

    #For blurr effect
    Frame = ['#D5C5BB']
    filler_blocks = []

    blurr_attribute_2 = ['#EFE3D7', '#B5ABA1']
    blurr_attribute_4 = ['#EDE2D0', '#B5A99B']
    blurr_attribute_8 = ['#EECAA8', '#FAE9D9']
    blurr_attribute_16 = ['#EFBBA2', '#FDE1D9']
    blurr_attribute_32 = ['#F3AF9C', '#FFE7DC']
    blurr_attribute_64 = ['#EFA393', '#EDF1DB']
    blurr_attribute_128 = ['#EBD7A4', '#FCEFCC']
    blurr_attribute_256 = ['#EDD6A2', '#EFE4CC']
    blurr_attribute_512 = ['#EDD693', '#FBECD3']
    blurr_attribute_1024 = ['#ECD589', '#FEEFC3']
    blurr_attribute_2048 = ['#ECD383', '#FCEEC1']
    blurr_attribute_4096 = ['#94918A', '#EFEAE0']




    # Creating round rectangle function:
    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2, x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)


    # FRAMES AND TEXTS

    Frame = round_rectangle(canvas_frame_coor[0][0], canvas_frame_coor[0][1], canvas_frame_coor[1][0],
                            canvas_frame_coor[1][1], radius=20, outline="#BCAEA5", fill="#BCAEA5")

    Score_Label_Frame = round_rectangle(canvas_frame_coor[0][0] + 310, canvas_frame_coor[0][1] - 220, 480, 110, radius=20,
                                        outline="#BCAEA5", fill="#BCAEA5")

    Score_Label_Frame1 = round_rectangle(canvas_frame_coor[0][0] + 480, canvas_frame_coor[0][1] - 220, 650, 110, radius=20,
                                         outline="#BCAEA5", fill="#BCAEA5")

    #


    Game_Label = canvas.create_text(canvas_frame_coor[0][0] + 100, canvas_frame_coor[0][1] - 180, text="2048",
                                    font="Helvetica 70 bold", fill=attribute_4[1])
    PlayerNameLabel = canvas.create_text(canvas_frame_coor[0][0] + 100, canvas_frame_coor[0][1] - 120, text=f"Hi, {PlayerName}!",
                                    font="Helvetica 20 bold", fill=attribute_4[1])
    Game_Label_instructions = canvas.create_text(canvas_frame_coor[0][0] + 280, canvas_frame_coor[0][1] - 30,
                                                 text="    Join the numbers and get to the 2048 tile!",
                                                 font="Helvetica 20 bold", fill=attribute_4[1])

    Score_Label = canvas.create_text(canvas_frame_coor[0][0] + 450, canvas_frame_coor[0][1] - 200,
                                     text="SCORE          BEST",
                                     font="Helvetica 20 bold", fill=attribute_4096[1])
    try:
        with open("highscore.csv", "r") as readThis:
            Scoress = [i.split(",") for i in readThis.readlines()]
            BestScore = canvas.create_text(canvas_frame_coor[0][0] + 540, canvas_frame_coor[0][1] - 160, text=Scoress[0][1],
                                           font="Helvetica 20 bold", fill="#ffffff")
    except:
        BestScore = canvas.create_text(canvas_frame_coor[0][0] + 540, canvas_frame_coor[0][1] - 160, text="0",
                                           font="Helvetica 20 bold", fill="#ffffff")
    # BestScore = canvas.create_text()
    Menu_Button = tk.Button(text="Back to menu", font="Helvetica 15 bold", bg="#BCAEA5", fg=attribute_4096[1],
                            activebackground="#BCAEA5", activeforeground=attribute_4096[1], underline=-1, relief="flat",
                            command=lambda: [root.destroy(), Main_Menu()])
    Menu_Button.pack()
    Menu_Button.place(x=425,
                      y=130, width=140, height=60)


    # for calibrating the distance between blocks

    # i = coorblocks
    # j = coorblock1...4
    # k = coorblock1...4
    def adjust_blocks():
        for i in range(len(coor_blocks)):
            for j in coor_blocks:
                j[i][0][0] += 8
                j[i][0][1] += 8

                j[i][1][0] -= 8
                j[i][1][1] -= 8


    adjust_blocks()


    # Filler blocks (Background)

    r1 = round_rectangle(coor_block1[0][0], coor_block1[0][1], coor_block1[1][0], coor_block1[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r2 = round_rectangle(coor_block2[0][0], coor_block2[0][1], coor_block2[1][0], coor_block2[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r3 = round_rectangle(coor_block3[0][0], coor_block3[0][1], coor_block3[1][0], coor_block3[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r4 = round_rectangle(coor_block4[0][0], coor_block4[0][1], coor_block4[1][0], coor_block4[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")

    r5 = round_rectangle(coor_block5[0][0], coor_block5[0][1], coor_block5[1][0], coor_block5[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r6 = round_rectangle(coor_block6[0][0], coor_block6[0][1], coor_block6[1][0], coor_block6[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r7 = round_rectangle(coor_block7[0][0], coor_block7[0][1], coor_block7[1][0], coor_block7[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r8 = round_rectangle(coor_block8[0][0], coor_block8[0][1], coor_block8[1][0], coor_block8[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")

    r9 = round_rectangle(coor_block9[0][0], coor_block9[0][1], coor_block9[1][0], coor_block9[1][1], radius=20,
                         outline="#CCC0B2", fill="#CCC0B2")
    r10 = round_rectangle(coor_block10[0][0], coor_block10[0][1], coor_block10[1][0], coor_block10[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")
    r11 = round_rectangle(coor_block11[0][0], coor_block11[0][1], coor_block11[1][0], coor_block11[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")
    r12 = round_rectangle(coor_block12[0][0], coor_block12[0][1], coor_block12[1][0], coor_block12[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")

    r13 = round_rectangle(coor_block13[0][0], coor_block13[0][1], coor_block13[1][0], coor_block13[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")
    r14 = round_rectangle(coor_block14[0][0], coor_block14[0][1], coor_block14[1][0], coor_block14[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")
    r15 = round_rectangle(coor_block15[0][0], coor_block15[0][1], coor_block15[1][0], coor_block15[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")
    r16 = round_rectangle(coor_block16[0][0], coor_block16[0][1], coor_block16[1][0], coor_block16[1][1], radius=20,
                          outline="#CCC0B2", fill="#CCC0B2")


    def is_FULL():
        flag = True
        for i in range(len(blocks)):
            for j in blocks[i]:
                if j == 0:
                    flag = False
        return flag


    def spawn_number():
        global blocks
        global Blockt1
        global random_block
        global random_block_label
        randomNum = random.choice(randomlist)
        if is_FULL() is False:
            random_row = random.choice(inducerlist)
            random_col = random.choice(inducerlist)
            if blocks[random_row][random_col] == 0:
                Blockt1[random_row][random_col] = randomNum
                blocks[random_row][random_col] = randomNum
                if randomNum == 2:
                    random_block = round_rectangle(coor_blocks[random_row][random_col][0][0],
                                                   coor_blocks[random_row][random_col][0][1],
                                                   coor_blocks[random_row][random_col][1][0],
                                                   coor_blocks[random_row][random_col][1][1],
                                                   radius=20, outline=attribute_2[0], fill=attribute_2[0])
                    random_block_label = canvas.create_text(
                        ((coor_blocks[random_row][random_col][0][0] + coor_blocks[random_row][random_col][1][0]) // 2,
                         (coor_blocks[random_row][random_col][0][1] + coor_blocks[random_row][random_col][1][1]) // 2),
                        text="2", font="Helvetica 45 bold", fill=attribute_2[1], tag="randomLabel")
                elif randomNum == 4:
                    random_block = round_rectangle(coor_blocks[random_row][random_col][0][0],
                                                   coor_blocks[random_row][random_col][0][1],
                                                   coor_blocks[random_row][random_col][1][0],
                                                   coor_blocks[random_row][random_col][1][1],
                                                   radius=20, outline=attribute_4[0], fill=attribute_4[0])
                    random_block_label = canvas.create_text(
                        ((coor_blocks[random_row][random_col][0][0] + coor_blocks[random_row][random_col][1][0]) // 2,
                         (coor_blocks[random_row][random_col][0][1] + coor_blocks[random_row][random_col][1][1]) // 2),
                        text="4", font="Helvetica 45 bold", fill=attribute_4[1])
            else:
                spawn_number()


    # For displaying score

    Score_Label_value = canvas.create_text(canvas_frame_coor[0][0] + 370, canvas_frame_coor[0][1] - 160, text=score,
                                           font="Helvetica 20 bold", fill=attribute_4096[1])


    # Displaying board...
    def display_board():
        global Block1, Block2, Block3, Block4, counterr
        global Score_Label_value
        global random_block, counter
        global random_block_label
        global block_1, block_1_label, block_2, block_2_label, block_3, block_3_label, block_4, block_4_label, block_5, block_5_label, block_6, block_6_label, block_7, block_7_label, block_8, block_8_label, block_9, block_9_label, block_10, block_11_label, block_12, block_12_label, block_13, block_13_label, block_14, block_14_label, block_15, block_15_label, block_16, block_16_label
        canvas.delete(Score_Label_value)
        Score_Label_value = canvas.create_text(canvas_frame_coor[0][0] + 370, canvas_frame_coor[0][1] - 160, text=score,
                                               font="Helvetica 20 bold", fill="#ffffff")

        k = 1  # K is the block number


        blocklist = blocks[0] + blocks[1] + blocks[2] + blocks[3]
        j = 0
        counter = 0

        if (not is_FULL() or is_combinable()) and (2048 not in blocklist):
            for i in blocklist:
                if i == 0:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                              Coor_blocks[j][1][1],
                                              radius=20, outline=attributes[0][0], fill=attributes[0][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text=" ", font="Helvetica 45 bold", fill=attributes[0][1])
                elif i == 2:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[1][0], fill=attributes[1][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="2", font="Helvetica 45 bold", fill=attributes[1][1])
                elif i == 4:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[2][0], fill=attributes[2][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="4", font="Helvetica 45 bold", fill=attributes[2][1])
                elif i == 8:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[3][0], fill=attributes[3][0])
                    canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="8", font="Helvetica 45 bold", fill=attributes[3][1])
                elif i == 16:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[4][0], fill=attributes[4][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="16", font="Helvetica 45 bold", fill=attributes[4][1])
                elif i == 32:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[5][0], fill=attributes[5][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="32", font="Helvetica 45 bold", fill=attributes[5][1])
                elif i == 64:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[6][0], fill=attributes[6][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="64", font="Helvetica 45 bold", fill=attributes[6][1])
                elif i == 128:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[7][0], fill=attributes[7][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="128", font="Helvetica 45 bold", fill=attributes[7][1])
                elif i == 256:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[8][0], fill=attributes[8][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="256", font="Helvetica 45 bold", fill=attributes[8][1])
                elif i == 512:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[9][0], fill=attributes[9][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="512", font="Helvetica 45 bold", fill=attributes[9][1])
                elif i == 1024:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[10][0], fill=attributes[10][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="1024", font="Helvetica 45 bold", fill=attributes[10][1])
                elif i == 2048:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0], Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=attributes[11][0], fill=attributes[11][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2, (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="2048", font="Helvetica 45 bold", fill=attributes[11][1])
                j+=1
        elif (2048 in blocklist) and counter == 0:
            counter += 1
            for i in blocklist:
                if i == 0:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20, outline=attributes[0][0], fill=attributes[0][0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text=" ", font="Helvetica 45 bold", fill=attributes[0][1])
                elif i == 2:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_2[0], fill=blurr_attribute_2[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="2", font="Helvetica 45 bold", fill=blurr_attribute_2[1])
                elif i == 4:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_4[0], fill=blurr_attribute_4[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="4", font="Helvetica 45 bold", fill=blurr_attribute_4[1])
                elif i == 8:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_8[0], fill=blurr_attribute_8[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="8", font="Helvetica 45 bold", fill=blurr_attribute_8[1])
                elif i == 16:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_16[0], fill=blurr_attribute_16[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="16", font="Helvetica 45 bold", fill=blurr_attribute_16[1])
                elif i == 32:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_32[0], fill=blurr_attribute_32[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="32", font="Helvetica 45 bold", fill=blurr_attribute_32[1])
                elif i == 64:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_64[0], fill=blurr_attribute_64[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="64", font="Helvetica 45 bold", fill=blurr_attribute_64[1])
                elif i == 128:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_128[0], fill=blurr_attribute_128[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="128", font="Helvetica 45 bold", fill=blurr_attribute_128[1])
                elif i == 256:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_256[0], fill=blurr_attribute_256[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="256", font="Helvetica 45 bold", fill=blurr_attribute_256[1])
                elif i == 512:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_512[0], fill=blurr_attribute_512[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="512", font="Helvetica 45 bold", fill=blurr_attribute_512[1])
                elif i == 1024:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_1024[0], fill=blurr_attribute_1024[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="1024", font="Helvetica 45 bold", fill=blurr_attribute_1024[1])
                elif i == 2048:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_2048[0], fill=blurr_attribute_2048[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="2048", font="Helvetica 45 bold", fill=blurr_attribute_2048[1])
                j += 1
            Game_Over_Label = canvas.create_text((canvas_frame_coor[0][0] + canvas_frame_coor[1][0]) // 2,
                                             (canvas_frame_coor[0][1] + canvas_frame_coor[1][1]) // 2,
                                             text="You win!",
                                             font="Helvetica 50 bold", fill='#7D6F60')
            Restart_Button = tk.Button(text="Try again", font="Helvetica 15 bold", bg="#907A63", fg="#F5ECE1",
                                       activebackground="#907A63", activeforeground="#F5ECE1", underline=-1,
                                       relief="flat", command=restart)
            Restart_Button.pack()

            Restart_Button.place(x=((canvas_frame_coor[0][0] + canvas_frame_coor[1][0]) // 2) - 130,
                                 y=((canvas_frame_coor[0][1] + canvas_frame_coor[1][1]) // 2) + 50, width=110,
                                 height=60)

            Menu_Button = tk.Button(text="Main menu", font="Helvetica 15 bold", bg="#907A63", fg="#F5ECE1",
                                    activebackground="#907A63", activeforeground="#F5ECE1", underline=-1, relief="flat", command=lambda:[root.destroy(), Main_Menu()])
            Menu_Button.pack()
            Menu_Button.place(x=((canvas_frame_coor[0][0] + canvas_frame_coor[1][0]) // 2) + 20,
                              y=((canvas_frame_coor[0][1] + canvas_frame_coor[1][1]) // 2) + 50, width=110, height=60)
            if counterr == 0:
                appendNewScore(PlayerName, score)
                counterr += 1

        elif counter == 0:
            for i in blocklist:
                if i == 2:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_2[0], fill=blurr_attribute_2[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="2", font="Helvetica 45 bold", fill=blurr_attribute_2[1])
                elif i == 4:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_4[0], fill=blurr_attribute_4[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="4", font="Helvetica 45 bold", fill=blurr_attribute_4[1])
                elif i == 8:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_8[0], fill=blurr_attribute_8[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="8", font="Helvetica 45 bold", fill=blurr_attribute_8[1])
                elif i == 16:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_16[0], fill=blurr_attribute_16[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="16", font="Helvetica 45 bold", fill=blurr_attribute_16[1])
                elif i == 32:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_32[0], fill=blurr_attribute_32[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="32", font="Helvetica 45 bold", fill=blurr_attribute_32[1])
                elif i == 64:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_64[0], fill=blurr_attribute_64[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="64", font="Helvetica 45 bold", fill=blurr_attribute_64[1])
                elif i == 128:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_128[0], fill=blurr_attribute_128[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="128", font="Helvetica 45 bold", fill=blurr_attribute_128[1])
                elif i == 256:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_256[0], fill=blurr_attribute_256[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="256", font="Helvetica 45 bold", fill=blurr_attribute_256[1])
                elif i == 512:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_512[0], fill=blurr_attribute_512[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="512", font="Helvetica 45 bold", fill=blurr_attribute_512[1])
                elif i == 1024:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_1024[0], fill=blurr_attribute_1024[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="1024", font="Helvetica 45 bold", fill=blurr_attribute_1024[1])
                elif i == 2048:
                    i = round_rectangle(Coor_blocks[j][0][0], Coor_blocks[j][0][1], Coor_blocks[j][1][0],
                                        Coor_blocks[j][1][1],
                                        radius=20,
                                        outline=blurr_attribute_2048[0], fill=blurr_attribute_2048[0])
                    i = canvas.create_text(
                        ((Coor_blocks[j][0][0] + Coor_blocks[j][1][0]) // 2,
                         (Coor_blocks[j][0][1] + Coor_blocks[j][1][1]) // 2),
                        text="2048", font="Helvetica 45 bold", fill=blurr_attribute_2048[1])
                j += 1
            Game_Over_Label = canvas.create_text((canvas_frame_coor[0][0] + canvas_frame_coor[1][0]) // 2,
                                             (canvas_frame_coor[0][1] + canvas_frame_coor[1][1]) // 2,
                                             text="Game over!",
                                             font="Helvetica 50 bold", fill='#7D6F60')
            Restart_Button = tk.Button(text ="Try again", font="Helvetica 15 bold", bg="#907A63", fg = "#F5ECE1", activebackground= "#907A63", activeforeground= "#F5ECE1", underline=-1, relief = "flat", command=restart)
            Restart_Button.pack()

            Restart_Button.place(x = ((canvas_frame_coor[0][0] + canvas_frame_coor[1][0]) // 2) - 130, y = ((canvas_frame_coor[0][1] + canvas_frame_coor[1][1]) // 2) + 50 , width = 110, height = 60)

            Menu_Button = tk.Button(text ="Main menu", font="Helvetica 15 bold", bg="#907A63", fg = "#F5ECE1", activebackground= "#907A63", activeforeground= "#F5ECE1", underline=-1, relief = "flat", command=lambda:[root.destroy(), Main_Menu()])
            Menu_Button.pack()
            Menu_Button.place(x = ((canvas_frame_coor[0][0] + canvas_frame_coor[1][0]) // 2) +20, y = ((canvas_frame_coor[0][1] + canvas_frame_coor[1][1]) // 2) + 50 , width = 110, height = 60)
            if counterr == 0:
                appendNewScore(PlayerName, score)
                counterr += 1


    # repositioning board
    def reposition_w():
        Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]

        Block1[:] = [Blockt1[3][0], Blockt1[2][0], Blockt1[1][0], Blockt1[0][0]]
        Block2[:] = [Blockt1[3][1], Blockt1[2][1], Blockt1[1][1], Blockt1[0][1]]
        Block3[:] = [Blockt1[3][2], Blockt1[2][2], Blockt1[1][2], Blockt1[0][2]]
        Block4[:] = [Blockt1[3][3], Blockt1[2][3], Blockt1[1][3], Blockt1[0][3]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    def reposition_a():
        Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]
        Block1[:] = [Blockt1[0][3], Blockt1[0][2], Blockt1[0][1], Blockt1[0][0]]
        Block2[:] = [Blockt1[1][3], Blockt1[1][2], Blockt1[1][1], Blockt1[1][0]]
        Block3[:] = [Blockt1[2][3], Blockt1[2][2], Blockt1[2][1], Blockt1[2][0]]
        Block4[:] = [Blockt1[3][3], Blockt1[3][2], Blockt1[3][1], Blockt1[3][0]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    def reposition_s():
        Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]
        Block1[:] = [Blockt1[0][0], Blockt1[1][0], Blockt1[2][0], Blockt1[3][0]]
        Block2[:] = [Blockt1[0][1], Blockt1[1][1], Blockt1[2][1], Blockt1[3][1]]
        Block3[:] = [Blockt1[0][2], Blockt1[1][2], Blockt1[2][2], Blockt1[3][2]]
        Block4[:] = [Blockt1[0][3], Blockt1[1][3], Blockt1[2][3], Blockt1[3][3]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    def reposition_d():
        Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]
        Block1[:] = [Blockt1[0][0], Blockt1[0][1], Blockt1[0][2], Blockt1[0][3]]
        Block2[:] = [Blockt1[1][0], Blockt1[1][1], Blockt1[1][2], Blockt1[1][3]]
        Block3[:] = [Blockt1[2][0], Blockt1[2][1], Blockt1[2][2], Blockt1[2][3]]
        Block4[:] = [Blockt1[3][0], Blockt1[3][1], Blockt1[3][2], Blockt1[3][3]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    # For repositioning Blocks
    def reposition_Block1():
        global Blockt1
        Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]
        for j in range(2):
            for i in reversed(range(0, 4)):
                if i == 3:
                    if Blockt1[0][i] == 0:
                        Blockt1[0][i] = Blockt1[0][i - 1]
                        Blockt1[0][i - 1] = Blockt1[0][i - 2]
                        Blockt1[0][i - 2] = Blockt1[0][i - 3]
                        Blockt1[0][i - 3] = 0
                elif i == 2:
                    if Blockt1[0][i] == 0:
                        Blockt1[0][i] = Blockt1[0][i - 1]
                        Blockt1[0][i - 1] = Blockt1[0][i - 2]
                        Blockt1[0][i - 2] = 0
                elif i == 1:
                    if Blockt1[0][i] == 0:
                        Blockt1[0][i] = Blockt1[0][i - 1]
                        Blockt1[0][i - 1] = 0


    def reposition_Block2():
        for j in range(2):
            for i in reversed(range(0, 4)):
                if i == 3:
                    if Blockt1[1][i] == 0:
                        Blockt1[1][i] = Blockt1[1][i - 1]
                        Blockt1[1][i - 1] = Blockt1[1][i - 2]
                        Blockt1[1][i - 2] = Blockt1[1][i - 3]
                        Blockt1[1][i - 3] = 0
                elif i == 2:
                    if Blockt1[1][i] == 0:
                        Blockt1[1][i] = Blockt1[1][i - 1]
                        Blockt1[1][i - 1] = Blockt1[1][i - 2]
                        Blockt1[1][i - 2] = 0
                elif i == 1:
                    if Blockt1[1][i] == 0:
                        Blockt1[1][i] = Blockt1[1][i - 1]
                        Blockt1[1][i - 1] = 0


    def reposition_Block3():
        for j in range(2):
            for i in reversed(range(0, 4)):
                if i == 3:
                    if Blockt1[2][i] == 0:
                        Blockt1[2][i] = Blockt1[2][i - 1]
                        Blockt1[2][i - 1] = Blockt1[2][i - 2]
                        Blockt1[2][i - 2] = Blockt1[2][i - 3]
                        Blockt1[2][i - 3] = 0
                elif i == 2:
                    if Blockt1[2][i] == 0:
                        Blockt1[2][i] = Blockt1[2][i - 1]
                        Blockt1[2][i - 1] = Blockt1[2][i - 2]
                        Blockt1[2][i - 2] = 0
                elif i == 1:
                    if Blockt1[2][i] == 0:
                        Blockt1[2][i] = Blockt1[2][i - 1]
                        Blockt1[2][i - 1] = 0


    def reposition_Block4():
        for j in range(2):
            for i in reversed(range(0, 4)):
                if i == 3:
                    if Blockt1[3][i] == 0:
                        Blockt1[3][i] = Blockt1[3][i - 1]
                        Blockt1[3][i - 1] = Blockt1[3][i - 2]
                        Blockt1[3][i - 2] = Blockt1[3][i - 3]
                        Blockt1[3][i - 3] = 0
                elif i == 2:
                    if Blockt1[3][i] == 0:
                        Blockt1[3][i] = Blockt1[3][i - 1]
                        Blockt1[3][i - 1] = Blockt1[3][i - 2]
                        Blockt1[3][i - 2] = 0
                elif i == 1:
                    if Blockt1[3][i] == 0:
                        Blockt1[3][i] = Blockt1[3][i - 1]
                        Blockt1[3][i - 1] = 0


    def reposition_blocks():
        reposition_Block1()
        Blockt1[:] = [Blockt1[0], Block2.copy(), Block3.copy(), Block4.copy()]
        reposition_Block2()
        Blockt1[:] = [Blockt1[0], Blockt1[1], Block3.copy(), Block4.copy()]
        reposition_Block3()
        Blockt1[:] = [Blockt1[0], Blockt1[1], Blockt1[2], Block4.copy()]
        reposition_Block4()


    # For combining blocks
    def Block1_combine():
        global Blockt1
        global score

        for i in reversed(range(0, 4)):
            if i == 3:
                if (Blockt1[0][i] == Blockt1[0][i - 1]) and Blockt1[0][i] != 0:
                    Blockt1[0][i] = Blockt1[0][i] + Blockt1[0][i - 1]
                    score += Blockt1[0][i]
                    Blockt1[0][i - 1] = Blockt1[0][i - 2]
                    Blockt1[0][i - 2] = Blockt1[0][i - 3]
                    Blockt1[0][i - 3] = 0
            elif i == 2:
                if (Blockt1[0][i] == Blockt1[0][i - 1]) and Blockt1[0][i] != 0:
                    Blockt1[0][i] = Blockt1[0][i] + Blockt1[0][i - 1]
                    score += Blockt1[0][i]
                    Blockt1[0][i - 1] = Blockt1[0][i - 2]
                    Blockt1[0][i - 2] = 0
            elif i == 1:
                if (Blockt1[0][i] == Blockt1[0][i - 1]) and Blockt1[0][i] != 0:
                    Blockt1[0][i] = Blockt1[0][i] + Blockt1[0][i - 1]
                    score += Blockt1[0][i] + Blockt1[0][i - 1]
                    Blockt1[0][i - 1] = 0


    def Block2_combine():
        global score
        for i in reversed(range(0, 4)):
            if i == 3:
                if (Blockt1[1][i] == Blockt1[1][i - 1]) and Blockt1[1][i] != 0:
                    Blockt1[1][i] = Blockt1[1][i] + Blockt1[1][i - 1]
                    score += Blockt1[1][i]
                    Blockt1[1][i - 1] = Blockt1[1][i - 2]
                    Blockt1[1][i - 2] = Blockt1[1][i - 3]
                    Blockt1[1][i - 3] = 0
            elif i == 2:
                if (Blockt1[1][i] == Blockt1[1][i - 1]) and Blockt1[1][i] != 0:
                    Blockt1[1][i] = Blockt1[1][i] + Blockt1[1][i - 1]
                    score += Blockt1[1][i]
                    Blockt1[1][i - 1] = Blockt1[1][i - 2]
                    Blockt1[1][i - 2] = 0
            elif i == 1:
                if (Blockt1[1][i] == Blockt1[1][i - 1]) and Blockt1[1][i] != 0:
                    Blockt1[1][i] = Blockt1[1][i] + Blockt1[1][i - 1]
                    score += Blockt1[1][i]
                    Blockt1[1][i - 1] = 0


    def Block3_combine():
        global score
        for i in reversed(range(0, 4)):
            if i == 3:
                if (Blockt1[2][i] == Blockt1[2][i - 1]) and Blockt1[2][i] != 0:
                    Blockt1[2][i] = Blockt1[2][i] + Blockt1[2][i - 1]
                    score += Blockt1[2][i]
                    Blockt1[2][i - 1] = Blockt1[2][i - 2]
                    Blockt1[2][i - 2] = Blockt1[2][i - 3]
                    Blockt1[2][i - 3] = 0
            elif i == 2:
                if (Blockt1[2][i] == Blockt1[2][i - 1]) and Blockt1[2][i] != 0:
                    Blockt1[2][i] = Blockt1[2][i] + Blockt1[2][i - 1]
                    score += Blockt1[2][i]
                    Blockt1[2][i - 1] = Blockt1[2][i - 2]
                    Blockt1[2][i - 2] = 0
            elif i == 1:
                if (Blockt1[2][i] == Blockt1[2][i - 1]) and Blockt1[2][i] != 0:
                    Blockt1[2][i] = Blockt1[2][i] + Blockt1[2][i - 1]
                    score += Blockt1[2][i]
                    Blockt1[2][i - 1] = 0


    def Block4_combine():
        global score
        for i in reversed(range(0, 4)):
            if i == 3:
                if (Blockt1[3][i] == Blockt1[3][i - 1]) and Blockt1[3][i] != 0:
                    Blockt1[3][i] = Blockt1[3][i] + Blockt1[3][i - 1]
                    score += Blockt1[3][i]
                    Blockt1[3][i - 1] = Blockt1[3][i - 2]
                    Blockt1[3][i - 2] = Blockt1[3][i - 3]
                    Blockt1[3][i - 3] = 0
            elif i == 2:
                if (Blockt1[3][i] == Blockt1[3][i - 1]) and Blockt1[3][i] != 0:
                    Blockt1[3][i] = Blockt1[3][i] + Blockt1[3][i - 1]
                    score += Blockt1[3][i]
                    Blockt1[3][i - 1] = Blockt1[3][i - 2]
                    Blockt1[3][i - 2] = 0
            elif i == 1:
                if (Blockt1[3][i] == Blockt1[3][i - 1]) and Blockt1[3][i] != 0:
                    Blockt1[3][i] = Blockt1[3][i] + Blockt1[3][i - 1]
                    score += Blockt1[3][i]
                    Blockt1[3][i - 1] = 0


    def combine_blocks():
        Block1_combine()
        Blockt1[:] = [Blockt1[0], Blockt1[1].copy(), Blockt1[2].copy(), Blockt1[3].copy()]

        Block2_combine()
        Blockt1[:] = [Blockt1[0], Blockt1[1], Blockt1[2].copy(), Blockt1[3].copy()]

        Block3_combine()
        Blockt1[:] = [Blockt1[0], Blockt1[1].copy(), Blockt1[2], Blockt1[3].copy()]

        Block4_combine()

        blocks[:] = Blockt1


    # for reverting blocks

    def revert_w():
        global Blockt1
        Block1[:] = [Blockt1[0][3], Blockt1[1][3], Blockt1[2][3], Blockt1[3][3]]
        Block2[:] = [Blockt1[0][2], Blockt1[1][2], Blockt1[2][2], Blockt1[3][2]]
        Block3[:] = [Blockt1[0][1], Blockt1[1][1], Blockt1[2][1], Blockt1[3][1]]
        Block4[:] = [Blockt1[0][0], Blockt1[1][0], Blockt1[2][0], Blockt1[3][0]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    def revert_a():
        global Blockt1
        Block1[:] = [Blockt1[0][3], Blockt1[0][2], Blockt1[0][1], Blockt1[0][0]]
        Block2[:] = [Blockt1[1][3], Blockt1[1][2], Blockt1[1][1], Blockt1[1][0]]
        Block3[:] = [Blockt1[2][3], Blockt1[2][2], Blockt1[2][1], Blockt1[2][0]]
        Block4[:] = [Blockt1[3][3], Blockt1[3][2], Blockt1[3][1], Blockt1[3][0]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    def revert_s():
        global Blockt1
        Block1[:] = [Blockt1[0][0], Blockt1[1][0], Blockt1[2][0], Blockt1[3][0]]
        Block2[:] = [Blockt1[0][1], Blockt1[1][1], Blockt1[2][1], Blockt1[3][1]]
        Block3[:] = [Blockt1[0][2], Blockt1[1][2], Blockt1[2][2], Blockt1[3][2]]
        Block4[:] = [Blockt1[0][3], Blockt1[1][3], Blockt1[2][3], Blockt1[3][3]]
        blocks[:] = [Block1, Block2, Block3, Block4]


    def revert_d():
        global Blockt1
        Block1[:] = [Blockt1[0][0], Blockt1[0][1], Blockt1[0][2], Blockt1[0][3]]
        Block2[:] = [Blockt1[1][0], Blockt1[1][1], Blockt1[1][2], Blockt1[1][3]]
        Block3[:] = [Blockt1[2][0], Blockt1[2][1], Blockt1[2][2], Blockt1[2][3]]
        Block4[:] = [Blockt1[3][0], Blockt1[3][1], Blockt1[3][2], Blockt1[3][3]]
        blocks[:] = [Block1, Block2, Block3, Block4]

    #Testing for combinability
    def is_combinable():
        flag = False
        i = 0
        repositions = [reposition_w, reposition_a, reposition_s, reposition_d]
        for j in range(len(repositions)):
            repositions[j]()
            for block in blocks:
                if block[i] == block[i+1]:
                    flag = True
                if block[i + 1] == block[i+2]:
                    flag = True
                if block[i + 2] == block[i+3]:
                    flag = True
        return flag

    # Event if WASD is pressed
    def kpress(event):
        global block_1, blocklist
        global block_1_label
        Blockt1 = [Block1.copy(), Block2.copy(), Block3.copy(), Block4.copy()]
        blockCopy = copy.deepcopy(blocks)
        blocklist = Block1 + Block2 + Block3 + Block4
        # delete_board()
        if event.char == ("w" or "W") and (2048 not in blocklist):
            reposition_w()
            reposition_blocks()
            combine_blocks()
            revert_w()

        elif event.char == ("a" or "A") and (2048 not in blocklist):
            reposition_a()
            reposition_blocks()
            combine_blocks()
            revert_a()

        elif event.char == ("s" or "S") and (2048 not in blocklist):

            reposition_s()
            reposition_blocks()
            combine_blocks()

            revert_s()

        elif event.char == ("d" or "D") and (2048 not in blocklist):
            reposition_d()
            reposition_blocks()
            combine_blocks()
            revert_d()

        if blockCopy != blocks:
            spawn_number()

        elif is_FULL() == True:
            blocklist = blocks[0] + blocks[1] + blocks[2] + blocks[3]

        global rn1
        global rn2

        display_board()


    def main_game():
        spawn_number()
        spawn_number()
        display_board()
        root.bind("<Key>", kpress)
        root.mainloop()



    # This is the main program
    main_game()




#Function for the main_game_window + Game Over window
def Leaderboards():
    W = 702
    H = 900



    root = tk.Tk()
    root.maxsize(W,H)
    root.minsize(W,H)
    root.title("2048")
    canvas = tk.Canvas(root, bg="#F8F8F0")  # Orig: #F8F8F0
    canvas.place(relwidth = 1, relheight = 1)

    Game_Label_1 = canvas.create_text(W-351, H-800, text="2048",
                                    font="Helvetica 90 bold", fill='#4C483D')
    Game_Label_2 = canvas.create_text(W-351, H-700, text="Leaderboards",
                                    font="Helvetica 60 bold underline", fill='#4C483D')

    Game_Label_Name = canvas.create_text(W-520, H-600, text="Name",
                                    font="Helvetica 15 bold", fill='#4C483D')
    Game_Label_Score = canvas.create_text(W-380, H-600, text="Score",
                                    font="Helvetica 15 bold", fill='#4C483D')

    Game_Label_Date = canvas.create_text(W-210, H-600, text="Date",
                                    font="Helvetica 15 bold", fill='#4C483D')
    Leaderboards_Frame = canvas.create_rectangle(50, 320, W-50, H-50, outline="#BCAEA5", fill="#BCAEA5")

    Rank1 = canvas.create_rectangle(25, 350, 75, 390, outline = "#C9B037", fill = "#C9B037")
    Rank1_Frame = canvas.create_rectangle(63, 340, W - 75, 410, outline="#CCC0B2", fill="#CCC0B2")
    Rank1_Label = canvas.create_text(45, 370, text="1", font="Helvetica 25 bold", fill="#FBF0EB")

    Rank2 = canvas.create_rectangle(25, 456, 75, 496, outline = "#B4B4B4", fill = "#B4B4B4")
    Rank2_Frame = canvas.create_rectangle(63, 440, W - 75, 510, outline="#CCC0B2", fill="#CCC0B2")
    Rank2_Label = canvas.create_text(45, 476, text="2", font="Helvetica 25 bold", fill="#FBF0EB")

    Rank3 = canvas.create_rectangle(25, 562, 75, 602, outline = "#6A3805", fill = "#6A3805")
    Rank3_Frame = canvas.create_rectangle(63, 550, W - 75, 620, outline="#CCC0B2", fill="#CCC0B2")
    Rank3_Label = canvas.create_text(45, 582, text="3", font="Helvetica 25 bold", fill="#FBF0EB")

    Rank4 = canvas.create_rectangle(25, 668, 75, 708, outline = "#AD8A56", fill = "#AD8A56")
    Rank4_Frame = canvas.create_rectangle(63, 650, W - 75, 720, outline="#CCC0B2", fill="#CCC0B2")
    Rank4_Label = canvas.create_text(45, 688, text="4", font="Helvetica 25 bold", fill="#FBF0EB")

    Rank5 = canvas.create_rectangle(25, 774, 75, 814, outline = "#AD8A56", fill = "#AD8A56")
    Rank5_Frame = canvas.create_rectangle(63, 760, W - 75, 830, outline="#CCC0B2", fill="#CCC0B2")
    Rank5_Label = canvas.create_text(45, 794, text="5", font="Helvetica 25 bold", fill="#FBF0EB")
    CoordinateLabels = [370, 476, 582, 688, 794]
    RankColors = ["#d4af37", "#868686", "#905923","#4C483D", "#7A6F6D"]
    num = 0
    try:
        with open("highscore.csv", "r+") as file:
            scores = [i.split(",") for i in file.readlines()]


            num = 0
        for row in scores:
            try:
                if (num <= 5):
                    canvas.create_text(310, CoordinateLabels[num] + 12.5, text = f"          {row[0]}    \t{row[1]}   \t{row[2]}", font="Helvetica 20 bold", fill=RankColors[num] )

                    num += 1

            except:
                pass
    except:
        pass



    Menu_Button = tk.Button(text="Back to menu", font="Helvetica 15 bold", bg="#BCAEA5", fg='#EEE4DA',
                            activebackground="#BCAEA5", activeforeground='#EEE4DA', underline=-1,
                            relief="flat",
                            command=lambda: [root.destroy(), Main_Menu()])
    Menu_Button.pack()
    Menu_Button.place(x=550,
                      y=10, width=140, height=60)


    root.mainloop()


def EnterName():
    W = 702
    H = 900

    root = tk.Tk()
    root.maxsize(W-150,H-220)
    root.minsize(W-150,H-220)
    root.title("2048")
    canvas = tk.Canvas(root, bg="#F8F8F0")  # Orig: #F8F8F0

    name = tk.Entry(root, text="Enter name", font="Helvetica 25 bold", justify="center", fg="#4C483D")
    def getName():
        global PlayerName
        if len(name.get()) <= 7:
            PlayerName = name.get()
            root.destroy()
            main_game_window()
        else:
            pass
    name.pack()
    EnterNameLabel = canvas.create_text(285, 275, text="ENTER NAME:", font="Helvetica 30 bold", fill="#4C483D")
    name.place(relx=0.145, rely=0.45, relwidth=500/702, relheight=125/900)
    PlayGame = tk.Button(text="PLAY 2048!", font="Helvetica 25 bold", bg="#907A63", fg="#F5ECE1",
                         activebackground="#907A63", activeforeground="#F5ECE1", underline=-1,
                         relief="flat", command = getName)
    PlayGame.pack()
    PlayGame.place(relx=0.25, rely=0.65, relwidth=360/702, relheight=125/900)
    canvas.place(relwidth = 1, relheight = 1)

    root.mainloop()






def Main_Menu():
    W = 702
    H = 900


    def Exit():
        exit(0)


    root = tk.Tk()
    root.maxsize(W,H)
    root.minsize(W-150, H-220)
    root.title("2048")

    canvas = tk.Canvas(root, bg="#F8F8F0")  # Orig: #F8F8F0
    canvas.place(relwidth= 1, relheight= 1)

    Game_Label_1 = canvas.create_text(370, 150, text="2048",
                                      font="Helvetica 100 bold underline", fill='#4C483D')

    # TOP LEFT
    Design_Black = tk.Frame( bg='#4C483D')
    Design_Black.place(relx = 0, rely = 0, relwidth = 150/900, relheight = 110/900)
    Design_Yellow = tk.Frame( bg='#ECC135')
    Design_Yellow.place(relx = 0.167, rely = 0, relwidth = 125/900, relheight = 80/900)
    Design_Yellow2 = tk.Frame(bg='#F0C64E')
    Design_Yellow2.place(relx=0.306, rely=0, relwidth=100 / 900, relheight=60 / 900)
    Design_Yellow3 = tk.Frame(bg='#EFCE71')
    Design_Yellow3.place(relx=0.417, rely=0, relwidth=75 / 900, relheight=40 / 900)
    Design_Orange = tk.Frame(bg='#F17C5A')
    Design_Orange.place(relx=0.5, rely=0, relwidth=50 / 900, relheight=27 / 900)
    Design_Orange1 = tk.Frame(bg='#F5B174')
    Design_Orange1.place(relx=0.556, rely=0, relwidth=25 / 900, relheight=17.5 / 900)
    Design_Yellow3 = tk.Frame(bg='#EBC544')
    Design_Yellow3.place(relx=0, rely=0.122, relwidth=113/900, relheight=95/900)
    Design_Yellow4 = tk.Frame(bg='#ECCC65')
    Design_Yellow4.place(relx=0, rely=0.228, relwidth=85 / 900, relheight=80 / 900)
    Design_Orange2 = tk.Frame(bg='#F75D3B')
    Design_Orange2.place(relx=0, rely=0.315, relwidth=58 / 900, relheight=63 / 900)
    Design_Red = tk.Frame(bg='#F29762')
    Design_Red.place(relx=0, rely=0.385, relwidth=39 / 900, relheight=41 / 900)
    Design_White = tk.Frame(bg='#ECE0CA')
    Design_White.place(relx=0, rely=0.431, relwidth=24 / 900, relheight=23 / 900)

    # BOTTOM RIGHT
    Design_Black = tk.Frame(bg='#4C483D')
    Design_Black.place(relx=0.833, rely=0.878, relwidth=150 / 900, relheight=110 / 900)
    Design_Yellow = tk.Frame(bg='#ECC135')
    Design_Yellow.place(relx=0.695, rely=0.911, relwidth=125 / 900, relheight=80 / 900)
    Design_Yellow2 = tk.Frame(bg='#F0C64E')
    Design_Yellow2.place(relx=0.584, rely=0.933, relwidth=100 / 900, relheight=60 / 900)
    Design_Yellow3 = tk.Frame(bg='#EFCE71')
    Design_Yellow3.place(relx=0.5, rely=0.955, relwidth=75 / 900, relheight=40 / 900)
    Design_Orange = tk.Frame(bg='#F17C5A')
    Design_Orange.place(relx=0.445, rely=0.972, relwidth=50 / 900, relheight=27 / 900)
    Design_Orange1 = tk.Frame(bg='#F5B174')
    Design_Orange1.place(relx=0.418, rely=0.98, relwidth=25 / 900, relheight=17.5 / 900)
    Design_Yellow3 = tk.Frame(bg='#EBC544')
    Design_Yellow3.place(relx=0.874, rely=0.772, relwidth=113 / 900, relheight=95 / 900)
    Design_Yellow4 = tk.Frame(bg='#ECCC65')
    Design_Yellow4.place(relx=0.91, rely=0.683, relwidth=85 / 900, relheight=80 / 900)
    Design_Orange2 = tk.Frame(bg='#F75D3B')
    Design_Orange2.place(relx=0.936, rely=0.613, relwidth=58 / 900, relheight=63 / 900)
    Design_Red = tk.Frame(bg='#F29762')
    Design_Red.place(relx=0.959, rely=0.568, relwidth=39 / 900, relheight=41 / 900)
    Design_Red = tk.Frame(bg='#ECE0CA')
    Design_Red.place(relx=0.976, rely=0.542, relwidth=24 / 900, relheight=23 / 900)


    Exit_Button = tk.Button(text="EXIT GAME", font="Helvetica 18 bold", bg="#4C483D", fg="#F5ECE1",
                               activebackground="#4C483D", activeforeground="#F5ECE1", underline=-1,
                               relief="flat", command=Exit)
    Exit_Button.pack()
    Exit_Button.place(relx = 52/702, rely = 750/900, relwidth = 400/900, relheight=118/900)

    Leaderboards_Button = tk.Button(text="LEADERBOARDS", font="Helvetica 18 bold", bg="#4C483D", fg="#F5ECE1",
                               activebackground="#4C483D", activeforeground="#F5ECE1", underline=-1,
                               relief="flat", command = lambda:[root.destroy(), Leaderboards()])
    Leaderboards_Button.pack()
    Leaderboards_Button.place(relx = 52/702, rely = 615/900, relwidth = 400/900, relheight=118/900)

    Play_Button = tk.Button(text="PLAY GAME", font="Helvetica 18 bold", bg="#4C483D", fg="#F5ECE1",
                               activebackground="#4C483D", activeforeground="#F5ECE1", underline=-1,
                               relief="flat", command = lambda:[root.destroy(), EnterName()])
    Play_Button.pack()
    Play_Button.place(relx = 52/702, rely = 475/900, relwidth = 400/900, relheight=118/900)

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2, y1 + radius, x2,
                  y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2, x2 - radius, y2, x1 + radius, y2,
                  x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1]

        return canvas.create_polygon(points, **kwargs, smooth=True)

    root.mainloop()
Main_Menu()