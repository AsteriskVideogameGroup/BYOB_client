from enum import IntEnum


class JoypadControl(IntEnum):

    """
                                   ____                            ____
                                  /AX2 \                          /AX5 \
                               __/_____\__                     __/_____\__
       Button 4    <-------   /___________\___________________/___________\   --------> Button 5
                             /  _______                                    \
                            /  / ____  \           __               Y       \
                           /  / / AX \ \       <|  |X| |>       x       B    \
                           |  \ \_01_/ /                            A        \
                            \  \______/                      _______         /
                             \               ^              / ____  \       /
                             /            < DPAD >         / / AX \ |       \
                            /                v             \ \34_/  /       \
                           /                 _____________  \______/        \
                          /                 |             |                 \
                          \                 |             |                 /
                           \                /              \               /
                            \              /                \             /
                             \            /                  \           /
                              \__________/                    \_________/
    
        Axis 0 ->  horizontal axis of AX01: 
    
        Axis 1 ->  vertical axis of AX01:  
    
        Axis 3 ->  horizontal axis of AX34: 
    
        Axis 4 ->  vertical axis of AX34:   
    
        Axis 2 and Axis 5 are the back triggers: 
    
        Y -> Button 3
    
        X -> Button 2
    
        A -> Button 0
    
        B -> Button 1
    
        LB -> Button 4
    
        RB -> Button 5
    
        <| select -> Button 6
    
        |> start -> Button 7        
         _                                       
        |X| -> Button 8
        
        AXIS01 (pressed) -> Button 9
        
        AXIS34 (pressed) -> Button 10
        
        DPAD -> Hat 0:               
    */


    """

    # Sticks
    AXIS0: int = 0
    AXIS1: int = 1
    AXIS2: int = 2
    AXIS3: int = 3
    AXIS4: int = 4
    AXIS5: int = 5

    # Buttons
    BUTTON0: int = 0
    BUTTON1: int = 1
    BUTTON2: int = 2
    BUTTON3: int = 3
    BUTTON4: int = 4
    BUTTON5: int = 5
    BUTTON6: int = 6
    BUTTON7: int = 7
    BUTTON8: int = 8
    BUTTON9: int = 9
    BUTTON10: int = 10

    # Hat
    DPAD: int = 0


