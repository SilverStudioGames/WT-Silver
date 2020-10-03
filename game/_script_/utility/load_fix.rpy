
init python:
    config.load_failed_label = "load_failed"
    config.after_load_callbacks.append(load_fix)

init -1 python:
    def load_fix():
        # Scan the call stack for missing labels
        # If a label is missing, assume a fatal error will occur eventually
        # Then wipe the stack and jump to config.load_failed_label to prevent the error
        context = renpy.game.context()
        script = renpy.game.script
        for i in xrange(-1, -len(context.return_stack)-1, -1):
            node = None

            if script.has_label(context.return_stack[i]):
                node = script.lookup(context.return_stack[i])
            elif script.has_label(context.call_location_stack[i]):
                node = script.lookup(context.call_location_stack[i]).next

            if node is None:
                # Clean up similar to RollbackLog.load_failed
                while renpy.exports.call_stack_depth():
                    renpy.exports.pop_call()

                renpy.game.contexts[0].force_checkpoint = True
                renpy.game.contexts[0].goto_label(renpy.config.load_failed_label)

                raise renpy.game.RestartTopContext()
                return

label load_failed:
    python:
        # Clear all screens and stop all sound
        renpy.scene("screens")
        for c in ["music", "bg_sounds", "weather"]:
            renpy.music.stop(c, 0.5)
        active_girl = None
    $ renpy.block_rollback() # Prevent rollback to broken past
    show screen blktone
    "Something went wrong while loading your save, but all is not lost! You will be back in the office with the same progress as when you saved the game. However, you can't rollback to a time before that moment."
    hide screen blktone
    with d5
    $ renpy.block_rollback() # Prevent rollback to this message
    jump main_room
