import fresh_tomatoes
import media

Captain_Underpants = media.Movie("Captain Underpants","George Beard and Harold Hutchins are two overly imaginative pranksters who spend hours in a treehouse creating comic books. When their mean principal threatens to separate them into different classes, the mischievous boys accidentally hypnotize him into thinking that he's a ridiculously enthusiastic, incredibly dimwitted superhero named Captain Underpants.","http://t3.gstatic.com/images?q=tbn:ANd9GcSe2w-CmmAEZb_hRRq2EGrl5G1PC0tn2snNDO-S9c__Jz66uRjC","https://www.youtube.com/watch?v=NP8TA3d_zvQ")
#print(Captain_Underpants.storyline)

Jumanji_Welcome_to_the_Jungle = media.Movie("Jumanji: Welcome to the Jungle", "Four high school kids discover an old video game console and are drawn into the game's jungle setting, literally becoming the adult avatars they chose. What they discover is that you don't just play Jumanji - you must survive it. To beat the game and return to the real world, they'll have to go on the most dangerous adventure of their lives, discover what Alan Parrish left 20 years ago, and change the way they think about themselves - or they'll be stuck in the game forever", "http://t3.gstatic.com/images?q=tbn:ANd9GcSJir3ifd1WldB6AfldmvA08D8jsv6t7ScNBeM5keJoE3CQsJa1","https://www.youtube.com/watch?v=sNGbd-i8wR0")
#print(Jumanji_Welcome_to_the_Jungle.storyline)

The_Lego_Batman_Movie = media.Movie("The Lego Batman Movie","There are big changes brewing in Gotham, but if Batman (Will Arnett) wants to save the city from the Joker's (Zach Galifianakis) hostile takeover, he may have to drop the lone vigilante thing, try to work with others and maybe, just maybe, learn to lighten up. Maybe his superhero sidekick Robin (Michael Cera) and loyal butler Alfred (Ralph Fiennes) can show him a thing or two.", "http://t1.gstatic.com/images?q=tbn:ANd9GcS-ysr5T3p--mS7aTE5KvaSnmM6CosK9_D-znWs_fbTNVgizHhv", "https://www.youtube.com/watch?v=ZQlfyj5bH-M")


The_LEGO_Ninjago_Movie = media.Movie("The LEGO Ninjago Movie","The battle for NINJAGO City calls to action young Master Builder Lloyd, aka the Green Ninja, along with his friends, also secret ninja warriors. Led by Master Wu, as wise-cracking as he is wise, they must defeat the evil warlord Garmadon, who also happens to be Lloyd's dad. Pitting father against son, the epic showdown tests these fierce but undisciplined modern-day ninjas as they learn to check their egos and pull together to unleash the inner power of Spinjitzu.","http://t0.gstatic.com/images?q=tbn:ANd9GcRIesCVWOiAc5bBYwhQuBzARQeuDxTQuBTeHHM442L61X_F78wl","https://www.youtube.com/watch?v=sZSYYiATFTI")

The_Emoji_Movie = media.Movie("The Emoji Movie","Hidden inside a smartphone, the bustling city of Textopolis is home to all emojis. Each emoji has only one facial expression, except for Gene, an exuberant emoji with multiple expressions. Determined to become normal like the other emojis, Gene enlists the help of his best friend Hi-5 and a notorious code breaker called Jailbreak. During their travels through the other apps, the three emojis discover a great danger that could threaten their phone's very existence.","http://t0.gstatic.com/images?q=tbn:ANd9GcRQc0pj8eAuiJa5K_DX1MeTSWwQCX5mDaBWz8auP38FeUX7NX5V","https://www.youtube.com/watch?v=o_nfdzMhmrA")

Despicable_Me_3 = media.Movie("Despicable Me 3","The mischievous Minions hope that Gru will return to a life of crime after the new boss of the Anti-Villain League fires him. Instead, Gru decides to remain retired and travel to Freedonia to meet his long-lost twin brother for the first time. The reunited siblings soon find themselves in an uneasy alliance to take down the elusive Balthazar Bratt, a former 1980s child star who seeks revenge against the world", "http://t1.gstatic.com/images?q=tbn:ANd9GcTg3JQThacqbSPauObMc700jNW_GTAd-e9DAV_QIWvMYq8v3mVx", "https://www.youtube.com/watch?v=UReNQAdei4Y")

The_LEGO_Ninjago_Movie = media.Movie("The LEGO Ninjago Movie","The battle for NINJAGO City calls to action young Master Builder Lloyd, aka the Green Ninja, along with his friends, also secret ninja warriors. Led by Master Wu, as wise-cracking as he is wise, they must defeat the evil warlord Garmadon, who also happens to be Lloyd's dad. Pitting father against son, the epic showdown tests these fierce but undisciplined modern-day ninjas as they learn to check their egos and pull together to unleash the inner power of Spinjitzu.","http://t0.gstatic.com/images?q=tbn:ANd9GcRIesCVWOiAc5bBYwhQuBzARQeuDxTQuBTeHHM442L61X_F78wl","https://www.youtube.com/watch?v=sZSYYiATFTI")

The_Emoji_Movie = media.Movie("The Emoji Movie","Hidden inside a smartphone, the bustling city of Textopolis is home to all emojis. Each emoji has only one facial expression, except for Gene, an exuberant emoji with multiple expressions. Determined to become normal like the other emojis, Gene enlists the help of his best friend Hi-5 and a notorious code breaker called Jailbreak. During their travels through the other apps, the three emojis discover a great danger that could threaten their phone's very existence.","http://t0.gstatic.com/images?q=tbn:ANd9GcRQc0pj8eAuiJa5K_DX1MeTSWwQCX5mDaBWz8auP38FeUX7NX5V","https://www.youtube.com/watch?v=o_nfdzMhmrA")

movies = [Captain_Underpants,The_LEGO_Ninjago_Movie, The_Emoji_Movie, Jumanji_Welcome_to_the_Jungle, The_Lego_Batman_Movie, Despicable_Me_3, ]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(The_Lego_Batman_Movie.storyline)
#The_Lego_Batman_Movie.show_trailer()