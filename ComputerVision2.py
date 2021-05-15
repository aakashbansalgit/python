import cv2
cap = cv2.VideoCapture(0) #give file name or provide device index
# while (cap.isOpened()) #if u give a file name
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.avi', fourcc, 20.0, (640,480))
while (cap.isOpened()):
    ret, frame = cap.read()
# u can use various properties and print them. link: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGNpTFhRRDltNnhva0ZEMHZzS0hXeDNBc18yUXxBQ3Jtc0trTFJOVmNJakZrSUVPTG4yZ3V1TllHZV9GbXgtZkNCTWE4cGxsRkFYVkZNX2NTOWMtOFlZY0NsWm1ZUHBzdEFMVkNYY2tXRXhnZ0k0c2RsTVlJYnJQdDRTNFJqUFZfZUFnd0VCel9yTlF3VXM0TkpIaw&q=https%3A%2F%2Fdocs.opencv.org%2F4.0.0%2Fd4%2Fd15%2Fgroup__videoio__flags__base.html%23gaeb8dd9c89c10a5c63c139bf7c4f5704d
    if ret == True:
        out.write(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()    
