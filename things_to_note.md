I would like to expand "client" to work with multiple characters. Basically creating a Character class that holds information
  about the person's background, and a log of messages between the player and this character.
  I'm not sure how to avoid saving the entirety of the conversation, and instead only saving the important bits. 
  Maybe a new chat.completion with a new sys prompt? Oh shit what if I use that langchain StrOutput thing to only get 1 line of text out, and the sys prompt to emphasize concise summaries

