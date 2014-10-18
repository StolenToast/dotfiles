#
# Instructions: bind a key with your format, for example:  /key bind meta-t /toggle_time %H:%M:%S
#
import weechat
def cmd_cb(data, buffer, args):
    if weechat.config_string(weechat.config_get('weechat.look.buffer_time_format')):
        args = ''
    weechat.command('', '/mute set weechat.look.buffer_time_format "%s"' % args)
    return weechat.WEECHAT_RC_OK
weechat.register('toggle_time', 'FlashCode', '0.1', 'GPL3', 'Toggle timestamp in buffers', '', '')
weechat.hook_command('toggle_time', '', '', '', '', 'cmd_cb', '')
