Here are the Excel formulas to generate the specified email permutations:

Assuming:

- **A2**: First Name (`elon`)
- **B2**: Last Name (`musk`)
- **C2**: Domain (`spacex.com`)

### Formulas

1. **elon@spacex.com**
   ```excel
   =A2 & "@" & C2
   ```

2. **musk@spacex.com**
   ```excel
   =B2 & "@" & C2
   ```

3. **elonmusk@spacex.com**
   ```excel
   =A2 & B2 & "@" & C2
   ```

4. **elon.musk@spacex.com**
   ```excel
   =A2 & "." & B2 & "@" & C2
   ```

5. **emusk@spacex.com**
   ```excel
   =LEFT(A2, 1) & B2 & "@" & C2
   ```

6. **e.musk@spacex.com**
   ```excel
   =LEFT(A2, 1) & "." & B2 & "@" & C2
   ```

7. **elonm@spacex.com**
   ```excel
   =A2 & LEFT(B2, 1) & "@" & C2
   ```

8. **elon.m@spacex.com**
   ```excel
   =A2 & "." & LEFT(B2, 1) & "@" & C2
   ```

9. **em@spacex.com**
   ```excel
   =LEFT(A2, 1) & LEFT(B2, 1) & "@" & C2
   ```

10. **e.m@spacex.com**
    ```excel
    =LEFT(A2, 1) & "." & LEFT(B2, 1) & "@" & C2
    ```

11. **muskelon@spacex.com**
    ```excel
    =B2 & A2 & "@" & C2
    ```

12. **musk.elon@spacex.com**
    ```excel
    =B2 & "." & A2 & "@" & C2
    ```

13. **muske@spacex.com**
    ```excel
    =B2 & LEFT(A2, 1) & "@" & C2
    ```

14. **musk.e@spacex.com**
    ```excel
    =B2 & "." & LEFT(A2, 1) & "@" & C2
    ```

15. **melon@spacex.com**
    ```excel
    =LEFT(B2, 1) & A2 & "@" & C2
    ```

16. **m.elon@spacex.com**
    ```excel
    =LEFT(B2, 1) & "." & A2 & "@" & C2
    ```

17. **me@spacex.com**
    ```excel
    =LEFT(B2, 1) & LEFT(A2, 1) & "@" & C2
    ```

18. **m.e@spacex.com**
    ```excel
    =LEFT(B2, 1) & "." & LEFT(A2, 1) & "@" & C2
    ```

19. **elon-musk@spacex.com**
    ```excel
    =A2 & "-" & B2 & "@" & C2
    ```

20. **e-musk@spacex.com**
    ```excel
    =LEFT(A2, 1) & "-" & B2 & "@" & C2
    ```

21. **elon-m@spacex.com**
    ```excel
    =A2 & "-" & LEFT(B2, 1) & "@" & C2
    ```

22. **e-m@spacex.com**
    ```excel
    =LEFT(A2, 1) & "-" & LEFT(B2, 1) & "@" & C2
    ```

23. **musk-elon@spacex.com**
    ```excel
    =B2 & "-" & A2 & "@" & C2
    ```

24. **musk-e@spacex.com**
    ```excel
    =B2 & "-" & LEFT(A2, 1) & "@" & C2
    ```

25. **m-elon@spacex.com**
    ```excel
    =LEFT(B2, 1) & "-" & A2 & "@" & C2
    ```

26. **m-e@spacex.com**
    ```excel
    =LEFT(B2, 1) & "-" & LEFT(A2, 1) & "@" & C2
    ```

27. **elon_musk@spacex.com**
    ```excel
    =A2 & "_" & B2 & "@" & C2
    ```

28. **e_musk@spacex.com**
    ```excel
    =LEFT(A2, 1) & "_" & B2 & "@" & C2
    ```

29. **elon_m@spacex.com**
    ```excel
    =A2 & "_" & LEFT(B2, 1) & "@" & C2
    ```

30. **e_m@spacex.com**
    ```excel
    =LEFT(A2, 1) & "_" & LEFT(B2, 1) & "@" & C2
    ```

31. **musk_elon@spacex.com**
    ```excel
    =B2 & "_" & A2 & "@" & C2
    ```

32. **musk_e@spacex.com**
    ```excel
    =B2 & "_" & LEFT(A2, 1) & "@" & C2
    ```

33. **m_elon@spacex.com**
    ```excel
    =LEFT(B2, 1) & "_" & A2 & "@" & C2
    ```

34. **m_e@spacex.com**
    ```excel
    =LEFT(B2, 1) & "_" & LEFT(A2, 1) & "@" & C2
    ```

You can copy and paste these formulas into Excel and use them to generate the email permutations for each name and domain combination you input.