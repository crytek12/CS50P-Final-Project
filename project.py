import pandas as pd
from random import choice
from pywebio.input import input
from pywebio.output import put_text, put_markdown


def main():
    sci_fi = [["andor", "action", "short", "series"],
        ["she-hulk: attorney at law", "action", "short", "series"],
        ["the munsters", "comedy", "long", "movie"],
        ["thor: love and thunder", "adventure", "long", "movie"],
        ["cyberpunk: edgerunners", "animation", "short", "series"],
        ["the handmaid's tale", "drama", "long", "series"],
        ["rick and morty", "animation", "long", "series"],
        ["stranger things", "fantasy", "long", "series"],
        ["american horror story", "drama", "long", "series"],
        ["quantum leap", "mystery", "short", "series"],
        ["the boys", "crime", "long", "series"],
        ["the sandman", "horror", "short", "series"],
        ["avatar", "fantasy", "long", "movie"],
        ["nope", "mystery", "long", "movie"],
        ["super pets", "adventure", "short", "movie"],
        ["vesper", "drama", "long", "movie"],
        ["everything everywhere all at once", "comedy", "long", "movie"],
        ["severance", "mystery", "short", "series"],
        ["black adam", "fantasy", "long", "movie"],
        ["see", "action", "long", "series"]]

    df = pd.DataFrame(sci_fi, columns=["name", "genre", "length", "type"])
    filtered_df = df.loc[(df.genre == genre()) & (df.length == runtime()) & (df.type == option())]
    put_markdown("# **Results**")
    try:
        put_markdown("You should watch:  **%s**" % choice(filtered_df["name"].tolist()))
    except IndexError:
        put_text("No match found")


def genre():
    group =  input("Input your genre")
    return group


def runtime():
    length = input("Input the length of the particular sci-fi")
    return length


def option():
    preference = input("Input whether Movies or series")
    return preference


if __name__ == "__main__":
    main()
