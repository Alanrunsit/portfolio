sent_message = "This is a secret don't let it get out."

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  file.seek(0)
  unsent_message = "This message has been unsent"
  file.truncate(len(unsent_message))
  file.write(unsent_message)

print("Original message:", sent_message)
print("Unsent message:", unsent_message)