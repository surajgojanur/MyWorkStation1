# Disk Format Guide

To completely reset (format) an external hard disk, you can use the `diskpart` tool, which allows you to manage your drives. Here's how you can do it:

### Warning: This will erase all data on the drive.

1. Open **Command Prompt** as **Administrator**.
    - Press **Windows + X** and select **Command Prompt (Admin)** or **Windows PowerShell (Admin)**.

2. Run the following commands:

    ```sh
    diskpart
    ```

3. In the `diskpart` prompt, list all disks connected to your system:

    ```sh
    list disk
    ```

4. Identify the external hard drive from the list. It will show all disks with their size, which can help you figure out the correct disk. Let's assume your external hard disk is **Disk 1**.

5. Select the external hard disk:

    ```sh
    select disk 1
    ```

    (Replace **1** with the correct disk number for your external drive.)

6. Now, clean the drive (this will remove all data and partitions):

    ```sh
    clean
    ```

7. Create a new partition:

    ```sh
    create partition primary
    ```

8. Format the drive (you can replace **NTFS** with **FAT32** or **exFAT** depending on your preference):

    ```sh
    format fs=ntfs quick
    ```

9. Assign a drive letter:

    ```sh
    assign
    ```

10. Exit `diskpart`:

     ```sh
     exit
     ```

After this, the external hard disk should be reset and formatted, ready for use.

Let me know if you face any issues!