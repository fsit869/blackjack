
import tkinter as tk
from tkinter import ttk
from view import IFrame, FrameUtilities, Image_label


class End_frame(IFrame.IFrame):
    def __init__(self, view, parent, root, top_level, style, callbacks):
        ''' Constructor to create Startup_frame
        ;:param view: View layer
        :param parent: Parent
        :param top_level: Toplevel
        :param style: Style
        '''
        super().__init__(view, parent, root, top_level, style, callbacks)
        self.set_frame_name()

        title_frame = ttk.Labelframe(self)
        title_frame.pack(pady=10, padx=40, fill=tk.X, )
        self.title = ttk.Label(title_frame, text="Game Results", style="title.default.TLabel")
        self.title.pack(pady=20)

        self.player_display_frame = ttk.Frame(self)
        self.player_display_frame.pack()

        ttk.Label(self.player_display_frame, text="Players:").grid(row=0, column=0)
        ttk.Label(self.player_display_frame, text="Status:").grid(row=0, column=1)
        ttk.Label(self.player_display_frame, text="Cards:").grid(row=0, column=2)

        _command_frame = ttk.Frame(self)
        _command_frame.pack(fill=tk.BOTH, pady=10, padx=40, expand=1, side=tk.BOTTOM)

        ttk.Button(_command_frame, text="Play Again", command=callbacks.get("start_frame")).pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=1)
        ttk.Button(_command_frame, text="Quit", command=self.callbacks.get("quit_program")).pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.BOTH, expand=1)

    def update_frame(self, dict):
        ''' Update end frame contents

        :param dict:
        :return:
        '''
        current_row = 2

        winner = dict.get("winner_name")
        players = dict.get("players")
        if players != None and winner != None:
            FrameUtilities.FrameUtitlies.destory_children(self.player_display_frame)
            ttk.Label(self.player_display_frame, text="Winner: " + winner).grid(row=1, column=0, columnspan=3)

            for player in players:
                name = player[0]
                status = player[1]
                cards = player[2]
                ttk.Label(self.player_display_frame, text=name).grid(row=current_row, column=0)
                ttk.Label(self.player_display_frame, text=status).grid(row=current_row, column=1)
                # ttk.Label(self.player_display_frame, text=cards).grid(row=current_row, column=2)
                current_column = 3
                for card in cards:
                    card = Image_label.Image_label(self.player_display_frame, card, card.IMAGELOCATION())
                    card.resize_image_width_pixel_ratio(80)
                    card.grid(row=current_row, column=current_column)
                    current_column += 1
                current_row += 1

    def set_frame_name(self):
        ''' Sets name of frame.

        :return:
        '''
        return "End_frame"

    def _resize_min_root(self):
        ''' Resize frame and apply min size

        :return:
        '''
        self.view.set_root_min_size(
            int(self.view.SCREEN_WIDTH/2),
            int(self.view.SCREEN_HEIGHT/2),
        )
        self.root
        self.top_level.state('zoomed')

