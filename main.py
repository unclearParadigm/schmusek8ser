import version

print(f"""
--------------------------------------------------------------------------------\033[1m
  /\_/\  (            _                              _    ___         v{version.VERSION}               
 ( ^.^ ) _) ___  ___| |__  _ __ ___  _   _ ___  ___ | | _( _ ) ___  ___ _ __ 
   \\"/  (  / __|/ __| '_ \\| '_ ` _ \\| | | / __|/ _ \\| |/ / _ \\/ __|/ _ \\ '__|
 ( | | )   \\__ \\ (__| | | | | | | | | |_| \\__ \\  __/|   < (_) \\__ \\  __/ |   
(__d b__)  |___/\\___|_| |_|_| |_| |_|\\__,_|___/\\___||_|\\_\\___/|___/\\___|_|\033[0m
--------------------------------------------------------------------------------
""".strip('\n'))


if __name__ == '__main__':
    import socketserver
    import utils.log as log
    from static import config
    from router import Router

    with socketserver.TCPServer((config.LISTEN_HOST, config.LISTEN_PORT), Router) as httpd:
        log.info(f'Server started listening to http://{config.LISTEN_HOST}:{config.LISTEN_PORT}')
        httpd.serve_forever()
