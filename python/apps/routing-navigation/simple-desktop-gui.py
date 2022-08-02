import flet
from tkinter import Tk
from tkinter import filedialog as fd
from flet import (
    AppBar,
    Page,
    Text,
    View,
    colors,
    FloatingActionButton,
    icons,
    Row,
    Column,
    TextField,
    Container,
    Dropdown,
    dropdown,
)


def main(page: Page):
    page.title = "OSINT Tool"
    page.window_center()

    def home_page():
        return Container(
            Row(
                [
                    FloatingActionButton(
                        autofocus=False,
                        tooltip="Import SDR",
                        icon=icons.ADD_CIRCLE_OUTLINE,
                        width=150,
                        height=150,
                        bgcolor=colors.WHITE70,
                        on_click=lambda _: page.go("/import_sdr_page"),
                    ),
                    FloatingActionButton(
                        autofocus=False,
                        tooltip="Search Tools",
                        icon=icons.SEARCH_OUTLINED,
                        width=150,
                        height=150,
                        bgcolor=colors.WHITE70,
                        on_click=lambda _: page.go("/sim_search_page"),
                    ),
                ],
                alignment="center",
                vertical_alignment="center",
            ),
            expand=True,
        )

    def import_sdr():
        return Row(
            [
                Container(
                    Column(
                        [
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Home",
                                icon=icons.HOME_ROUNDED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/"),
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
                Container(
                    Column(
                        [
                            Row(
                                [
                                    Dropdown(
                                        options=[
                                            dropdown.Option(
                                                "Select Operator", disabled=True
                                            ),
                                            dropdown.Option("AIRTEL"),
                                            dropdown.Option("BSNL"),
                                            dropdown.Option("JIO"),
                                            dropdown.Option("VI"),
                                        ],
                                        width=500,
                                        prefix_icon=icons.CELL_TOWER,
                                    )
                                ],
                                alignment="center",
                            ),
                            Row(
                                [
                                    TextField(
                                        prefix_icon=icons.FILE_OPEN,
                                        width=500,
                                        on_focus=lambda _: fd.askopenfilename(),
                                    ),
                                ],
                                alignment="center",
                            ),
                        ],
                        alignment="center",
                    ),
                    expand=True,  # bgcolor=colors.AMBER_100
                ),
                # Container(
                #     Column(
                #             [
                #                 TextField(prefix_icon=icons.INFO, width=500, multiline=True, max_lines=35)
                #             ], alignment="start",
                #     ), bgcolor=colors.AMBER_100
                # )
            ],
            alignment="start",
            vertical_alignment="start",
        )

    def selectfile():
        file_name = fd.askopenfilename()
        return file_name

    def search_sim():
        return Row(
            [
                Container(
                    Column(
                        [
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Home",
                                icon=icons.HOME_ROUNDED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="SIM Search",
                                icon=icons.SIM_CARD_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/sim_search_page"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Aadhar Search",
                                icon=icons.ACCOUNT_CIRCLE_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/aadhar_search_page"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="IMEI Search",
                                icon=icons.SMARTPHONE_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/imei_search_page"),
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
                Container(
                    Column(
                        [
                            Row(
                                [
                                    TextField(
                                        hint_text="Enter mobile number",
                                        width=500,
                                        autofocus=True,
                                        prefix_icon=icons.SIM_CARD,
                                    ),
                                ]
                            ),
                            Row(
                                [
                                    TextField(
                                        prefix_icon=icons.INFO,
                                        width=500,
                                        multiline=True,
                                        max_lines=35,
                                    ),
                                ]
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
                # Container(
                #     Column(
                #             [
                #                 TextField(prefix_icon=icons.INFO, width=500, multiline=True, max_lines=35)
                #             ], alignment="start",
                #     ), bgcolor=colors.AMBER_100
                # )
            ],
            alignment="start",
            vertical_alignment="start",
        )

    def search_aadhar():
        return Row(
            [
                Container(
                    Column(
                        [
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Home",
                                icon=icons.HOME_ROUNDED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="SIM Search",
                                icon=icons.SIM_CARD_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/sim_search_page"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Aadhar Search",
                                icon=icons.ACCOUNT_CIRCLE_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/aadhar_search_page"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="IMEI Search",
                                icon=icons.SMARTPHONE_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/imei_search_page"),
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
                Container(
                    Column(
                        [
                            Row(
                                [
                                    TextField(
                                        hint_text="Enter Aadhar number",
                                        width=500,
                                        multiline=True,
                                        max_lines=35,
                                        autofocus=True,
                                        prefix_icon=icons.ACCOUNT_CIRCLE,
                                    ),
                                ]
                            ),
                            Row(
                                [
                                    TextField(
                                        prefix_icon=icons.INFO,
                                        width=500,
                                        multiline=True,
                                        max_lines=35,
                                    ),
                                ]
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
            ],
            alignment="start",
            vertical_alignment="start",
        )

    def search_imei():
        return Row(
            [
                Container(
                    Column(
                        [
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Home",
                                icon=icons.HOME_ROUNDED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="SIM Search",
                                icon=icons.SIM_CARD_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/sim_search_page"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="Aadhar Search",
                                icon=icons.ACCOUNT_CIRCLE_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/aadhar_search_page"),
                            ),
                            FloatingActionButton(
                                autofocus=False,
                                tooltip="IMEI Search",
                                icon=icons.SMARTPHONE_OUTLINED,
                                width=50,
                                height=50,
                                bgcolor=colors.WHITE70,
                                on_click=lambda _: page.go("/imei_search_page"),
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
                Container(
                    Column(
                        [
                            Row(
                                [
                                    TextField(
                                        hint_text="Enter IMEI number",
                                        width=500,
                                        multiline=True,
                                        max_lines=35,
                                        autofocus=True,
                                        prefix_icon=icons.SMARTPHONE,
                                    ),
                                ]
                            ),
                            Row(
                                [
                                    TextField(
                                        prefix_icon=icons.INFO,
                                        width=500,
                                        multiline=True,
                                        max_lines=35,
                                    ),
                                ]
                            ),
                        ],
                        alignment="start",
                    ),  # bgcolor=colors.AMBER_100
                ),
            ],
            alignment="start",
            vertical_alignment="start",
        )

    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=colors.SURFACE_VARIANT),
                    home_page(),
                ],
            )
        )
        if page.route == "/import_sdr_page":
            page.views.append(
                View(
                    "/import_sdr_page",
                    [
                        AppBar(
                            title=Text("Import SDR"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        import_sdr(),
                    ],
                )
            )

        elif page.route == "/sim_search_page":
            page.views.append(
                View(
                    "/sim_search_page",
                    [
                        AppBar(
                            title=Text("SIM Search Tool"),
                            bgcolor=colors.SURFACE_VARIANT,
                        ),
                        search_sim(),
                    ],
                )
            )

        elif page.route == "/aadhar_search_page":
            page.views.append(
                View(
                    "/aadhar_search_page",
                    [
                        AppBar(
                            title=Text("Aadhar Search Tool"),
                            bgcolor=colors.SURFACE_VARIANT,
                        ),
                        search_aadhar(),
                    ],
                )
            )

        elif page.route == "/imei_search_page":
            page.views.append(
                View(
                    "/imei_search_page",
                    [
                        AppBar(
                            title=Text("IMEI Search Tool"),
                            bgcolor=colors.SURFACE_VARIANT,
                        ),
                        search_imei(),
                    ],
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main)
Tk().withdraw()
