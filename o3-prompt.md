**Task**
Write a copy of the popular game Wordle that users can play in the terminal; no GUI. It will include a feature the original does not have - a recommendation engine. Give me all necessary files, then explain how it works and tell me how to play.

**Description**
Use Python. Use object-oriented programming. You may produce more than one file - structure the project however you see fit. Use the same rules as the original game. For the word list (the list of words the target word is chosen from), use the actual word list if you have it. If not, approximate one yourself.

After each guess, ask the user if they would like a recommendation for their next guess. The recommendation engine should not have knowledge of the actual target word. It should consider all available letters, all eliminated letters, and the overall word list and recommend the top 10 words ranked by how efficiently it narrows the space of possible target words. 

If the user does not want a recommendation, continue the game as normal. When the game ends, give the user the option to play again.