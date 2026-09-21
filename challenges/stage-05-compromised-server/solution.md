# Stage 5 Solution

## Intended Solution Path

1. Enter the Stage 5 challenge container as the `analyst` user.

2. Confirm the current user and working directory:

```bash
whoami
pwd
```

Expected user:

```text
analyst
```

Expected working directory:

```text
/home/analyst
```

3. Inspect the authentication log:

```bash
cat /var/log/auth.log
```

The log shows failed authentication attempts followed by a successful SSH login for the `analyst` account from:

```text
10.13.37.22
```

It also contains evidence that `/opt/novatech/recovery-note.txt` was accessed.

4. Inspect the analyst's shell history:

```bash
cat ~/.bash_history
```

The history identifies the recovery note as an important artifact:

```text
cat /opt/novatech/recovery-note.txt
```

5. Inspect the recovery note:

```bash
cat /opt/novatech/recovery-note.txt
```

6. Recover the Stage 5 flag:

```text
SHADOW{compromised_server_traced}
```

7. Recover the vault token:

```text
NV-SV-6204
```

8. Record the next-stage clue:

```text
NEXT: Use the recovered vault token in the final ShadowVault stage.
```

The vault token is required for Stage 6.
