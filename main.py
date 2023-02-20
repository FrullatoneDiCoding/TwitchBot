from multiprocessing import Process
from bot import Bot
from time import sleep
from datetime import datetime

emptyDict = {}


class ListenBot(Bot):
    def action(self, username, msg):
      now = datetime.now()
      f = open("logfile.txt", "a")
      f.write(self.channel+"\n")
      f.write(f"{now.hour}:{now.minute}:{now.second} - {username} -> {msg}\n")
      f.close()




channels = ["#cadutosullavoro", "#gianfrancosbirboni"]

# bot = ListenBot(channel="#cadutosullavoro")
if __name__ == "__main__":
  bots = []

  for channel in channels:
    bot = ListenBot(channel=channel)
    p = Process(target=bot.run)
    p.start()
    bots.append(p)

  for b in bots:
    b.join()

# for channel in channels:
#     bot=ListenBot(channel=channel)
#     bots.append(bot)
# for bot in bots:
#     bot.run()
