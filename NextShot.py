import datetime
import locale
# this sets the format code to German
locale.setlocale(locale.LC_ALL, 'de_DE')

# date of last shot
lastshot_input = input('Wann war deine letzte Spritze? (Format: TT.MM.JJJJ)\n')
last_shot = datetime.datetime.strptime(lastshot_input, '%d.%m.%Y')

# interval of every shot in weeks
interval_input = int(input('In welchem Interval bekommst du deine Spritzen? (In Wochen)\n'))
interval = datetime.timedelta(weeks=interval_input)

# projected date of next shot
next_shot = last_shot + interval

# strftime decodes how the date will be displayed to the user
print('Deine nächste Spritze ist am ' + str(next_shot.strftime('%A, den %d. %B %Y.')))