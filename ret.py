def ret_message(in_msg):
    msg = in_msg.split()
    
    try:
    
        if msg[1] == "repeat":
            return msg[2]
        
        if msg[1] == "emu":
            return "Wonderhoi~ Wonderhoi~"
    
    except BaseException:
        return "Unknown Input"
