import discord

def calculate_win_rate(wins, losses: int) -> float:
    total_games = wins + losses
    return (wins / total_games) * 100

def create_rank_embed(
        solo_rank:dict,
        flex_rank: dict |None
) -> discord.Embed:
    wins = solo_rank["wins"]
    losses = solo_rank["losses"]

    win_rate = calculate_win_rate(wins, losses)

    if flex_rank is not None:
        flex_wins = flex_rank["wins"]
        flex_losses = flex_rank["losses"]
        flex_win_rate = calculate_win_rate(flex_wins, flex_losses)


    tier = solo_rank["tier"]



    if tier == "IRON":
        rank_color = discord.Color.dark_gray()

    elif tier == "BRONZE":
        rank_color = discord.Color.from_rgb(205, 127, 50)
    elif tier == "SILVER":
        rank_color = discord.Color.from_rgb(192, 192, 192)
    elif tier == "GOLD":
        rank_color = discord.Color.from_rgb(255, 215, 0)
    elif tier == "PLATINUM":
        rank_color = discord.Color.from_rgb(0, 200, 225)
    elif tier == "DIAMOND":
        rank_color = discord.Color.from_rgb(0, 100, 200)
    elif tier == "MASTER":
        rank_color = discord.Color.from_rgb(128, 0, 128)
    elif tier == "GRANDMASTER":
        rank_color = discord.Color.from_rgb(255, 0, 0)
    elif tier == "CHALLENGER":
        rank_color = discord.Color.from_rgb(0, 200, 225)
    else:
        rank_color = discord.Color.default()    


    embed = discord.Embed(
        title="LoL Solo Rank" ,
        color=rank_color
    )

    embed.add_field(
        name="ランク",
        value=solo_rank["tier"] + " " + solo_rank["rank"],
        inline=False
    )

    embed.add_field(
        name="LP",
        value=str(solo_rank["leaguePoints"]),
        inline=True
    )

    embed.add_field(
        name="勝利",
        value=str(wins),
        inline=True
    )

    embed.add_field(
        name="敗北",
        value=str(losses),
        inline=True
    )

    embed.add_field(
        name="勝率",
        value=str(round(win_rate, 1)) + "%",
        inline=True
    )

    if flex_rank is not None:
        embed.add_field(
            name="Flex Queue",
            value=(
                flex_rank["tier"] + " " + flex_rank["rank"] + "\n"
                + str(flex_rank["leaguePoints"]) + " LP\n"
                + str(flex_wins) + "勝" + str(flex_losses) + "敗\n"
                + "勝率: " + str(round(flex_win_rate, 1)) + "%"

            ),
            inline=False
        )
    else:
        embed.add_field(
            name="Flex Queue",
            value ="ランクなし",
            inline=False

        )
    return embed

def create_recent_embed(summary, recent_message):
    embed = discord.Embed(
        title="LoL Recent Matches",
        description=summary + recent_message,
        color=discord.Color.blue()

    )
    return embed

def create_mastery_embed(
        mastery_message: str
) -> discord.Embed:
    mastery_embed = discord.Embed(
        title="LoL Champion Mastery",
        description=mastery_message,
        color=discord.Color.blue()
    )
    return mastery_embed    

def create_stats_embed(
    games_count: int,
    wins_count: int,
    losses_count: int,
    recent_result: str,
    average_kills: float,
    average_deaths: float,
    average_assists: float,
    average_cs: float,
    win_rate: float,
    champion_message: str,
    top_champion_message: str,
) -> discord.Embed:
    stats_embed = discord.Embed(
        title="LoL Recent Stats",
        color=discord.Color.blue()
    )

    stats_embed.add_field(
        name="直近試合",
        value=str(games_count) + "試合",
        inline=False
    )

    stats_embed.add_field(
        name="直近成績",
        value=(
            str(wins_count)
            + "勝 "
            + str(losses_count)
            + "敗 "
            + "("
            + recent_result
            + ")"
        ),
        inline=False
    )

    stats_embed.add_field(
        name="平均KDA",
        value=(
            str(round(average_kills, 1))
            + " / "
            + str(round(average_deaths, 1))
            + " / "
            + str(round(average_assists, 1))
        ),
        inline=False
    )

    stats_embed.add_field(
        name="平均CS",
        value=str(round(average_cs, 1)),
        inline=False
    )

    stats_embed.add_field(
        name="勝率",
        value=str(round(win_rate, 1)) + "%",
        inline=False
    )

    stats_embed.add_field(
        name="使用チャンピオン",
        value=champion_message,
        inline=False
    )

    stats_embed.add_field(
        name="最多使用",
        value=top_champion_message,
        inline=False
    )

    return stats_embed

def create_ingame_embed(
        ally_message: str,
        enemy_message: str
) -> discord.Embed:
    ingame_embed = discord.Embed(
        title="LoL In-Game",
        color=discord.Color.blue()
    )

    ingame_embed.add_field(
        name="味方チーム",
        value=ally_message,
        inline=False
    )

    ingame_embed.add_field(
        name="敵チーム",
        value=enemy_message,
        inline=False
    )

    return ingame_embed

def create_help_embed():
    embed = discord.Embed(
        title="LoL Bot Help",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="Quote Commands",
        value=(
            "!quote <champ>\n"
            "!quote random\n"
            "!quote list <champ>\n"
            "!champions\n"
            "!count"
        ),
        inline=False
    )

    embed.add_field(
        name="Riot Commands",
        value=(
            "!rank <name#tag>\n"
            "!recent <name#tag>\n"
            "!mastery <name#tag>\n"
            "!stats <name#tag>\n"
            "!ingame <name#tag>"
        ),
        inline=False
    )

    embed.add_field(
        name="Other",
        value="!github <username>",
        inline=False
    )

    return embed    
