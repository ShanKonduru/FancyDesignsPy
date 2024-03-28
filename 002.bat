@echo off
if '%1'=='1' goto ONE
if '%1'=='2' goto TWO
if '%1'=='3' goto THREE
if '%1'=='4' goto FOUR
if '%1'=='5' goto FIVE
if '%1'=='6' goto SIX
if '%1'=='7' goto SEVEN
if '%1'=='8' goto EIGHT
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

:SIX
poetry run python bifurcationdiagram.py
goto END

:SEVEN
poetry run python 3dbifurcation.py
goto END

:EIGHT
poetry run python ComplexNumbers3D.py
goto END


:USAGE
echo Usage:
echo "002 1 => to Run Flower design"
echo "002 2 => to Run flower2 design"
echo "002 3 => to Run concentric_circles design"
echo "002 4 => to Run spirograph design"
echo "002 5 => to Run spiralweb design"
echo "002 6 => to Run bifurcationdiagram design"
echo "002 7 => to Run 3dbifurcation design"
echo "002 8 => to Run ComplexNumbers3D design"
goto END

:END
