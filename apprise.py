import apprise
# Create an Apprise object
# Add the Telegram plugin with your chat ID
apobj = apprise.Apprise()
apobj.add('tgram://6616158083:AAHtonO5JDKR0hqVQtDEruIYNlmk22bU2WU')
# apobj.add('tgram://872936279')
# Send a notification to the specified chat ID
apobj.notify(
    body='IT is working nice',
    title='my notification title',
)
with apprise.LogCapture(level=apprise.logging.INFO) as output:
    # Send our notification
    apobj.notify(title="hello", body="world")

    # At this point of our code, we can have a look at our output
    # to see all of the logging that surrounded our notification(s)
    # Note that `output` is a StringIO object:
    print(output.getvalue())
#6616158083:AAHtonO5JDKR0hqVQtDEruIYNlmk22bU2WU
