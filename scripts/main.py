import genanki
import yaml

with open("./data/model.yaml", "r", encoding="utf-8") as file:
    model_config = yaml.safe_load(file)

model = genanki.Model(
    model_config["model"]["id"],
    model_config["model"]["name"],
    fields=[{"name": field} for field in model_config["model"]["fields"]],
    templates=[
        {
            "name": model_config["model"]["template"]["name"],
            "qfmt": model_config["model"]["template"]["qfmt"],
            "afmt": model_config["model"]["template"]["afmt"],
        }
    ],
)

with open("./data/deck.yaml", "r", encoding="utf-8") as file:
    deck_config = yaml.safe_load(file)

deck = genanki.Deck(
    deck_config["deck"]["id"],
    deck_config["deck"]["name"]
)

with open("./data/cards.yaml", "r", encoding="utf-8") as file:
    card_config = yaml.safe_load(file)

for card in card_config["cards"]:
    note = genanki.Note(
        model=model,
        fields=[card["question"], card["answer"]]
    )
    deck.add_note(note)

genanki.Package(deck).write_to_file("Hindi.apkg")
