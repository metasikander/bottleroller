from bottle import Bottle, template, request
import roll

index_html = '''
<html>
  <head>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      
      <title>Bottleroller</title>
      
      <style>
        .footer {
          position: fixed;
          left: 0;
          bottom: 0;
          width: 100%;
          text-align: center;
          position: relative;
        }

        p {font-family: Arial, Helvetica, sans-serif;}
      </style>
  </head>
  <body>
    <form method="post" action="/">
        <fieldset>
            <legend>Dice Thrower</legend>
            <ul>
                <li>Dice: <input name='dice'>
                </li>
            </ul><input type='submit' value='Throw Dice'>
        </fieldset>
    <INPUT TYPE="button" onClick="history.go(0)" VALUE="Reroll">
    </form>
    <p><b>Example: 2d8 +6 +d8</b></p>
    
    <p><b>Your Throw:</b> {{throw}}</p>
    <p>{{result}}</p>

  </body>

  <div class="footer">
    <p>Based on Dice-Roller by <a href="https://gitlab.xirion.net/vroest/dice-roller">Victor Roest</a><br>
    <a href="https://github.com/metasikander/bottleroller">Github project page</a></p>
  </div> 
</html>
'''

app = Bottle()

@app.route('/')
def index():
    """Main Page"""

    return template(index_html, result="Result here", throw=None)

@app.route('/', method="POST")
def formhandler():
    """Handle the form submission"""

    dice = request.forms.get('dice')

    result = "Result: " + str(roll.dice_roller(dice))

    return template(index_html, result=result, throw=dice)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, server='gunicorn', workers=4, debug=True)

# Found bugs:
# - no input in the form results in an error
# - wrong formating (2d20 +5 d8 works in cli)

#TODO:
# - Formatting of result: split out the result from the throw
# - Add reroll button (and/or reload page without question)
# - Add history
# - Make it possible to do a roll from google sheets
