@echo off
if '%1'=='1' goto ONE
if '%1'=='2' goto TWO
if '%1'=='3' goto THREE
if '%1'=='4' goto FOUR
if '%1'=='5' goto FIVE
goto USAGE

:ONE
poetry run python flower.py
goto END

:TWO
poetry run python flower2.py
goto END

:THREE 
poetry run python concentric_circles.py
goto END

:FOUR
poetry run python spirograph.py
goto END

:FIVE
poetry run python spiralweb.py
goto END

:USAGE
echo Usage:
echo "002 1 => to Run Flower design"
echo "002 2 => to Run flower2 design"
echo "002 3 => to Run concentric_circles design"
echo "002 4 => to Run spirograph design"
echo "002 5 => to Run spiralweb design"
goto END

:END
