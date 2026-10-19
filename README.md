# Workspace Repair Lab

Small, standard-library Python tools for diagnosing development environments and demonstrating safe, reversible troubleshooting. Python 3.10+ with venv support required.

## Run

```powershell
python doctor.py
python lab.py
python -m unittest -v
```

`doctor.py` inventories tool availability without executing those tools. It does not prove Docker, Git, WSL or Copilot works. No credentials, environment-variable values, usernames or absolute paths are included in the report.

`lab.py` reproduces a missing-module error using a synthetic dependency in a disposable virtual environment. The same import succeeds when run with that environment's interpreter. It installs nothing from the internet, leaves the existing Python installation unchanged, and removes its temporary environment afterward. The command uses isolated Python mode to avoid unrelated local packages.

This demonstrates interpreter/dependency mismatch, not a verified fix for a specific GitHub issue, VS Code bug, or customer incident. Windows/WSL interoperability and actual VS Code debug/test workflows need separate validation.

## Related implementation support

Richard Jones is developing fixed-scope Windows development-workspace troubleshooting services around these tools. Proposed engagement: one authorized computer, one project, agreed acceptance tests, a change log and rollback notes. Paid work requires a separate written scope and quote. No guaranteed repair of upstream defects, license problems or corporate policy restrictions.

Initial service: Python interpreter and virtual-environment diagnosis. Additional Git, workspace-performance, Docker/WSL and Copilot services require case-specific assessment; this repository does not demonstrate successful repairs in those areas yet.

Service and commercial-license inquiries: [IAMDIGITAL.ENT@GMAIL.COM](mailto:IAMDIGITAL.ENT@GMAIL.COM?subject=Workspace%20Repair%20Lab%20Inquiry). Do not email passwords, tokens, remote-access codes or unredacted logs. Public issues are for reproducible defects in this repository, not private customer intake.

## Safety boundaries

- No credential collection, remote access, admin elevation, firewall changes or TLS bypass.
- No WSL networking changes or restarts without specific approval.
- Never delete customer venvs, Git work, Docker volumes or settings as a default repair.
- Back up authorized files before a repair; prove recovery and document remaining limitations.
- Review reports before sharing. Inventory is not a security audit.

## Reference cases

Historical reports illustrate problem categories, not paid leads or defects we claim to have fixed:

- Python activation: https://github.com/microsoft/vscode-python-environments/issues/1341
- WSL interpreter mismatch: https://github.com/microsoft/vscode-python/issues/18015
- Docker startup: https://github.com/docker/for-win/issues/14781
- Copilot certificate errors: https://github.com/orgs/community/discussions/108295
- VS Code performance: https://github.com/microsoft/vscode/issues/245802
- Performance methodology: https://github.com/microsoft/vscode/wiki/performance-issues
- Git authentication tooling: https://github.com/git-ecosystem/git-credential-manager

## License

Source-available for limited evaluation under [LICENSE.txt](LICENSE.txt), version 1.0. This is **not an open-source license**. Private study and non-production evaluation are permitted; production use, paid client work, resale, sublicensing and redistribution require separate written permission, subject to the stated legal and hosting-platform exceptions. No support or warranty is included.

Licensor: Richard Jones. The public contact email is not a representation that a corporation or LLC exists. This project was developed with AI assistance; copyright is reserved only to the extent legally held. See [OWNER_LICENSE_GUIDE.md](OWNER_LICENSE_GUIDE.md) for review limitations and release safeguards. No upstream source code was intentionally copied; third-party rights remain separate.
