# Stage 6 Solution

## Intended Solution Path

1. Recover the vault recovery token from Stage 5:

`NV-SV-6204`

2. Inspect the supplied recovery-service evidence:

`evidence/vault-access.log`

3. Locate the verification fragments:

- FRAGMENT-A = 73
- FRAGMENT-B = 86
- FRAGMENT-C = 54

4. Convert each decimal value to its ASCII character:

- 73 -> I
- 86 -> V
- 54 -> 6

5. Preserve A-B-C ordering and combine the characters:

`IV6`

6. Start the Stage 6 recovery gateway and access it through the assigned local port.

7. Submit both authorization factors:

- Recovery Token: `NV-SV-6204`
- Verification Code: `IV6`

8. The gateway validates both values. If either value is incorrect, access is denied with HTTP 403.

9. When both values are correct, the gateway returns HTTP 200 and reveals the final flag:

`SHADOW{shadowvault_recovered}`

## Validation

The following authorization combinations were tested:

- Wrong token + correct code -> HTTP 403
- Correct token + wrong code -> HTTP 403
- Correct token + correct code -> HTTP 200

Therefore, both authorization factors are required to complete Stage 6.

## Final Result

Operation ShadowVault is completed when the participant successfully derives the verification code, combines it with the Stage 5 recovery token, and recovers the final flag.
