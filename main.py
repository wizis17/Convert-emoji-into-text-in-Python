import demoji

quotes = """Life is a rollercoaster 🎢 with moments of joy 😊, sadness 😢, 
                and everything in between. But through it all, remember to chase your dreams 🌟
                and never give up 💪."""

# Replace emojis with their descriptions
emojis = demoji.findall(quotes) 

print("Original quotes: ", quotes)
print()
for emoji in emojis:
    print(f"{emoji}: {emojis[emoji]}")