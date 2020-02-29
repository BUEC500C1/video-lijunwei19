import subprocess

def imgToVideo(username):
  fileName =  'processed_imgs/'+username +'_'+'img' +'%d'+'.png'

  avi =  "video/" + username + "normal.avi"
  mp4 =  "video/" + username + "better.mp4"


  subprocess.call(['ffmpeg', '-framerate', '0.3', '-i', 
    fileName, 
    avi])

  subprocess.call(['ffmpeg', '-i', avi, '-c:a', 'copy', 
    '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
    mp4])

def main():
  imgToVideo('IBM')

if __name__ == '__main__':
  main()