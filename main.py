import multiprocessing
import frontend
import time

def plot_points_from_input(pipe):
    pipe.send((23, 23))
    print("Point sent to UI")

if __name__ == "__main__":
    # Create a Pipe for communication with the UI process
    main_pipe, ui_pipe = multiprocessing.Pipe()

    # Start the Tkinter UI in a separate process
    ui_process = multiprocessing.Process(target=frontend.run_ui, args=(ui_pipe,))
    ui_process.start()

    # Wait for a short time to allow the UI process to update
    time.sleep(5)

    # Plot points from input in the main process
    plot_points_from_input(main_pipe)

    # Close the pipe to signal the end of communication
    #main_pipe.close()

    # Wait for the UI process to finish
    #ui_process.join()
