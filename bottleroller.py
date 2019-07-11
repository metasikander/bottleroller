from bottle import Bottle, template, request
import roll

index_html = '''
<html>
  <head>
      <title>Form Example</title>
  </head>
  <body>
    <form method="post" action="/">
        <fieldset>
            <legend>SAMPLE FORM</legend>
            <ul>
                <li>Dice: <input name='dice'>
                </li>
            </ul><input type='submit' value='Throw Dice'>
        </fieldset>
    </form>

    <p>{{result}}</p>

  </body>
</html>
'''

app = Bottle()

@app.route('/')
def index():
    """Home Page"""

    return template(index_html, result="Result here")

@app.route('/', method="POST")
def formhandler():
    """Handle the form submission"""

    dice = request.forms.get('dice')

    result = "Result: " + str(roll.dice_roller(dice))

    return template(index_html, result=result)

if __name__ == '__main__':
    app.run(host='localhost', port=8080, server='gunicorn', workers=4, debug=True)

# Found bugs:
# - typing help and help() in the form stalls the server
# - no input in the form results in an error

#TODO:
# - Formatting of result
