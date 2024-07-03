import unittest

from prreport import *

class TestPRReport(unittest.TestCase):
    def test_compute_relevant_diff(self):
        diff1 = '''
        From f7a22ec09f3a418e4946109f4aad9d0c837e60a1 Mon Sep 17 00:00:00 2001
From: "dependabot[bot]" <49699333+dependabot[bot]@users.noreply.github.com>
Date: Wed, 5 Jun 2024 06:32:05 +0000
Subject: [PATCH 1/2] build(deps): bump
 github.com/oasisprotocol/oasis-sdk/client-sdk/go

Bumps [github.com/oasisprotocol/oasis-sdk/client-sdk/go](https://github.com/oasisprotocol/oasis-sdk)
from 0.8.2 to 0.8.3.
- [Commits](https://github.com/oasisprotocol/oasis-sdk/compare/runtime-sdk/v0.8.2...runtime-sdk/v0.8.3)

---
updated-dependencies:
- dependency-name: github.com/oasisprotocol/oasis-sdk/client-sdk/go
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] <support@github.com>
---
 go.mod |  6 +++---
 go.sum | 12 ++++++------
 2 files changed, 9 insertions(+), 9 deletions(-)

diff --git a/go.mod b/go.mod
index d20978b..197bce9 100644
--- a/go.mod
+++ b/go.mod
@@ -21,7 +21,7 @@ require (
 	github.com/oasisprotocol/deoxysii v0.0.0-20220228165953-2091330c22b7
 	github.com/oasisprotocol/metadata-registry-tools v0.0.0-20220406100644-7e9a2b991920
 	github.com/oasisprotocol/oasis-core/go v0.2300.11
-	github.com/oasisprotocol/oasis-sdk/client-sdk/go v0.8.2
+	github.com/oasisprotocol/oasis-sdk/client-sdk/go v0.8.3
 	github.com/olekukonko/tablewriter v0.0.5
 	github.com/spf13/cobra v1.8.0
 	github.com/spf13/pflag v1.0.5
@@ -112,7 +112,7 @@ require (
 	github.com/sagikazarmark/locafero v0.4.0 // indirect
 	github.com/sagikazarmark/slog-shim v0.1.0 // indirect
 	github.com/sergi/go-diff v1.2.0 // indirect
-	github.com/shopspring/decimal v1.3.1 // indirect
+	github.com/shopspring/decimal v1.4.0 // indirect
 	github.com/skeema/knownhosts v1.2.1 // indirect
 	github.com/sourcegraph/conc v0.3.0 // indirect
 	github.com/spaolacci/murmur3 v1.1.0 // indirect
@@ -135,7 +135,7 @@ require (
 	golang.org/x/text v0.16.0 // indirect
 	golang.org/x/tools v0.21.1-0.20240508182429-e35e4ccd0d2d // indirect
 	google.golang.org/genproto/googleapis/rpc v0.0.0-20240314234333-6e1732d8331c // indirect
-	google.golang.org/grpc v1.62.1 // indirect
+	google.golang.org/grpc v1.63.2 // indirect
 	google.golang.org/grpc/security/advancedtls v0.0.0-20221004221323-12db695f1648 // indirect
 	google.golang.org/protobuf v1.33.0 // indirect
 	gopkg.in/ini.v1 v1.67.0 // indirect
diff --git a/go.sum b/go.sum
index e912ca7..d8caf9c 100644
--- a/go.sum
+++ b/go.sum
@@ -424,8 +424,8 @@ github.com/oasisprotocol/metadata-registry-tools v0.0.0-20220406100644-7e9a2b991
 github.com/oasisprotocol/metadata-registry-tools v0.0.0-20220406100644-7e9a2b991920/go.mod h1:MKr/giwakLyCCjSWh0W9Pbaf7rDD1K96Wr57OhNoUK0=
 github.com/oasisprotocol/oasis-core/go v0.2300.11 h1:YBkBSyLDMDWv3yoYEJ8WUPuumqFJsMNZWb71MXCKLmk=
 github.com/oasisprotocol/oasis-core/go v0.2300.11/go.mod h1:6BzLqNrFtX85fbEeNeq7oGOS/mF/z1EjIYSe739jOzQ=
 '''
        self.assertEqual(compute_relevant_diff(diff1), 6)

        diff2 = '''
        From c1350a74fc01102600bf5a2e8d6cac1680666b85 Mon Sep 17 00:00:00 2001
From: =?UTF-8?q?Matev=C5=BE=20Jekovec?= <matevz@oasisprotocol.org>
Date: Thu, 28 Mar 2024 16:51:29 +0100
Subject: [PATCH 1/5] docs: Revamp manage-tokens chapters

---
 README.md                                     |   10 +
 docs/dapp/cipher/README.mdx                   |    2 +-
 docs/dapp/emerald/README.mdx                  |    2 +-
 .../integrating-band-oracle-smart-contract.md |    2 +-
 .../dapp/emerald/writing-dapps-on-emerald.mdx |    4 +-
 docs/dapp/sapphire/README.mdx                 |    2 +-
 .../oasisscan_account_details.png             |  Bin 45925 -> 141974 bytes
 .../oasisscan_paratime_tx_details.png         |  Bin 0 -> 156605 bytes
 .../manage-tokens/oasisscan_paratime_txes.png |  Bin 0 -> 126646 bytes
 .../manage-tokens/oasisscan_validators.png    |  Bin 0 -> 183868 bytes
 .../paratime-deposit-withdraw/oasisscan1.png  |  Bin 74386 -> 0 bytes
 .../paratime-deposit-withdraw/oasisscan2.png  |  Bin 82340 -> 0 bytes
 .../transfer_deposit_withdrawal.svg           | 1483 +++++++++++++++++
 .../images/wallet/ext/create_wallet.png       |  Bin 0 -> 29036 bytes
 .../ledger1.png}                              |  Bin
 .../ledger2.png}                              |  Bin
 .../ledger3.png}                              |  Bin
 ...tx_ledger.jpg => ledger_oasis_approve.jpg} |  Bin
 .../ledger/live_allow_ledger_manager.png      |  Bin 45549 -> 55868 bytes
 .../images/wallet/ledger/live_oasis_app.png   |  Bin 39691 -> 0 bytes
 .../images/wallet/ledger/live_search_apps.png |  Bin 91292 -> 134551 bytes
 .../live_search_results_oasis_install.png     |  Bin 69808 -> 76786 bytes
 .../wallet/ledger/live_unlock_ledger.png      |  Bin 48327 -> 55227 bytes
 .../wallet/ledger/wallet_ext_import1.png      |  Bin 15786 -> 0 bytes
 .../ledger/wallet_web_account_address.png     |  Bin 69845 -> 0 bytes
 .../wallet/ledger/wallet_web_open_ledger.png  |  Bin 54111 -> 0 bytes
 .../ledger/wallet_web_open_ledger_account.png |  Bin 90096 -> 0 bytes
 ...et_web_received_rose_on_ledger_account.png |  Bin 97226 -> 0 bytes
 .../wallet_web_select_accounts_to_open.png    |  Bin 90691 -> 0 bytes
 ...allet_web_select_ledger_device_connect.png |  Bin 94902 -> 0 bytes
 .../ledger/wallet_web_send_confirm_tx.png     |  Bin 105211 -> 0 bytes
 .../wallet/ledger/wallet_web_send_rose.png    |  Bin 88263 -> 0 bytes
 .../ledger/wallet_web_send_verify_balance.png |  Bin 121070 -> 0 bytes
 docs/general/images/wallet/web/01_home.png    |  Bin 70103 -> 0 bytes
 .../wallet/web/02_this_is_your_mnemonic.png   |  Bin 90992 -> 0 bytes
 .../wallet/web/03_confirm_your_mnemonic.png   |  Bin 40824 -> 0 bytes
 .../wallet/web/04_how_to_open_your_wallet.png |  Bin 31343 -> 0 bytes
 .../wallet/web/05.1_open_with_mnemonics.png   |  Bin 40313 -> 0 bytes
 .../wallet/web/05.2_open_with_private_key.png |  Bin 24217 -> 0 bytes
 .../06_toogle_between_light_and_dark_mode.png |  Bin 72394 -> 0 bytes
 .../images/wallet/web/07_light_mode.png       |  Bin 72592 -> 0 bytes
 .../images/wallet/web/08_select_language.png  |  Bin 69565 -> 0 bytes
 .../wallet/web/account-popup-theme-dark.png   |  Bin 0 -> 91516 bytes
 .../images/wallet/web/active_delegations.png  |  Bin 78523 -> 0 bytes
 docs/general/images/wallet/web/buy.png        |  Bin 0 -> 127960 bytes
 .../web/create_new_wallet_mnemonic1.png       |  Bin 0 -> 177422 bytes
 .../web/create_new_wallet_mnemonic2.png       |  Bin 0 -> 201590 bytes
 .../web/create_new_wallet_select_accounts.png |  Bin 0 -> 154857 bytes
 docs/general/images/wallet/web/delegate1.png  |  Bin 0 -> 155974 bytes
 docs/general/images/wallet/web/delegate2.png  |  Bin 0 -> 146519 bytes
 docs/general/images/wallet/web/delegate3.png  |  Bin 0 -> 155664 bytes
 docs/general/images/wallet/web/deposit1.png   |  Bin 0 -> 128589 bytes
 docs/general/images/wallet/web/deposit2.png   |  Bin 0 -> 129440 bytes
 docs/general/images/wallet/web/deposit3.png   |  Bin 0 -> 125694 bytes
 docs/general/images/wallet/web/deposit4.png   |  Bin 0 -> 150057 bytes
 docs/general/images/wallet/web/deposit5.png   |  Bin 0 -> 134708 bytes
 docs/general/images/wallet/web/home.png       |  Bin 0 -> 111925 bytes
 .../images/wallet/web/import_wallet.png       |  Bin 0 -> 77349 bytes
 .../wallet/web/import_wallet_ledger.png       |  Bin 0 -> 53537 bytes
 .../wallet/web/import_wallet_mnemonic.png     |  Bin 0 -> 162052 bytes
 .../wallet/web/import_wallet_private_key.png  |  Bin 0 -> 98477 bytes
 .../wallet/web/no-profile-dark-theme.png      |  Bin 0 -> 113064 bytes
 docs/general/images/wallet/web/paratimes.png  |  Bin 0 -> 150872 bytes
 .../wallet/web/settings-my-accounts.png       |  Bin 0 -> 102697 bytes
 docs/general/images/wallet/web/stake.png      |  Bin 0 -> 160506 bytes
 docs/general/images/wallet/web/transfer.png   |  Bin 0 -> 154523 bytes
 .../general/images/wallet/web/undelegate1.png |  Bin 0 -> 161477 bytes
 .../general/images/wallet/web/undelegate2.png |  Bin 0 -> 152334 bytes
 .../general/images/wallet/web/undelegate3.png |  Bin 0 -> 149584 bytes
 docs/general/images/wallet/web/wallet.png     |  Bin 0 -> 137994 bytes
 docs/general/images/wallet/web/withdraw1.png  |  Bin 0 -> 128963 bytes
 docs/general/images/wallet/web/withdraw2.png  |  Bin 0 -> 134596 bytes
 docs/general/images/wallet/web/withdraw3.png  |  Bin 0 -> 126375 bytes
 docs/general/images/wallet/web/withdraw4.png  |  Bin 0 -> 151100 bytes
 docs/general/images/wallet/web/withdraw5.png  |  Bin 0 -> 134307 bytes
 docs/general/manage-tokens/README.mdx         |  196 ++-
 docs/general/manage-tokens/faq.mdx            |    4 +-
 .../holding-rose-tokens/custody-providers.md  |   34 +-
 .../holding-rose-tokens/ledger-wallet.md      |  180 +-
 ...-transfer-eth-erc20-to-emerald-paratime.md |    2 +-
 .../how-to-transfer-rose-into-paratime.mdx    |  250 ---
 .../manage-tokens/oasis-wallets/README.mdx    |   41 -
 .../oasis-wallets/browser-extension.md        |   83 -
 .../oasis-wallets/browser-extension.mdx       |  266 +++
 .../manage-tokens/oasis-wallets/web.md        |  127 --
 .../manage-tokens/oasis-wallets/web.mdx       |  391 +++++
 .../manage-tokens/staking-and-delegating.md   |  111 +-
 docs/general/manage-tokens/terminology.md     |    3 +
 docs/general/oasis-network/why-oasis.md       |   47 +-
 .../previous-upgrades/mainnet-upgrade.md      |    2 +-
 docs/node/run-your-node/validator-node.mdx    |    2 +-
 redirects.ts                                  |    7 +-
 sidebarGeneral.ts                             |   24 +-
 93 files changed, 2579 insertions(+), 696 deletions(-)
 create mode 100644 docs/general/images/manage-tokens/oasisscan_paratime_tx_details.png
 create mode 100644 docs/general/images/manage-tokens/oasisscan_paratime_txes.png
 create mode 100644 docs/general/images/manage-tokens/oasisscan_validators.png
 delete mode 100644 docs/general/images/manage-tokens/paratime-deposit-withdraw/oasisscan1.png
 delete mode 100644 docs/general/images/manage-tokens/paratime-deposit-withdraw/oasisscan2.png
 create mode 100644 docs/general/images/manage-tokens/transfer_deposit_withdrawal.svg
 create mode 100644 docs/general/images/wallet/ext/create_wallet.png
 rename docs/general/images/wallet/{ledger/wallet_ext_accounts_ledger.png => ext/ledger1.png} (100%)
 rename docs/general/images/wallet/{ledger/wallet_ext_import2.png => ext/ledger2.png} (100%)
 rename docs/general/images/wallet/{ledger/wallet_ext_import3.png => ext/ledger3.png} (100%)
 rename docs/general/images/wallet/ledger/{wallet_web_send_confirm_tx_ledger.jpg => ledger_oasis_approve.jpg} (100%)
 delete mode 100644 docs/general/images/wallet/ledger/live_oasis_app.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_ext_import1.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_account_address.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_open_ledger.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_open_ledger_account.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_received_rose_on_ledger_account.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_select_accounts_to_open.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_select_ledger_device_connect.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_send_confirm_tx.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_send_rose.png
 delete mode 100644 docs/general/images/wallet/ledger/wallet_web_send_verify_balance.png
 delete mode 100644 docs/general/images/wallet/web/01_home.png
 delete mode 100644 docs/general/images/wallet/web/02_this_is_your_mnemonic.png
 delete mode 100644 docs/general/images/wallet/web/03_confirm_your_mnemonic.png
 delete mode 100644 docs/general/images/wallet/web/04_how_to_open_your_wallet.png
 delete mode 100644 docs/general/images/wallet/web/05.1_open_with_mnemonics.png
 delete mode 100644 docs/general/images/wallet/web/05.2_open_with_private_key.png
 delete mode 100644 docs/general/images/wallet/web/06_toogle_between_light_and_dark_mode.png
 delete mode 100644 docs/general/images/wallet/web/07_light_mode.png
 delete mode 100644 docs/general/images/wallet/web/08_select_language.png
 create mode 100644 docs/general/images/wallet/web/account-popup-theme-dark.png
 delete mode 100644 docs/general/images/wallet/web/active_delegations.png
 create mode 100644 docs/general/images/wallet/web/buy.png
 create mode 100644 docs/general/images/wallet/web/create_new_wallet_mnemonic1.png
 create mode 100644 docs/general/images/wallet/web/create_new_wallet_mnemonic2.png
 create mode 100644 docs/general/images/wallet/web/create_new_wallet_select_accounts.png
 create mode 100644 docs/general/images/wallet/web/delegate1.png
 create mode 100644 docs/general/images/wallet/web/delegate2.png
 create mode 100644 docs/general/images/wallet/web/delegate3.png
 create mode 100644 docs/general/images/wallet/web/deposit1.png
 create mode 100644 docs/general/images/wallet/web/deposit2.png
 create mode 100644 docs/general/images/wallet/web/deposit3.png
 create mode 100644 docs/general/images/wallet/web/deposit4.png
 create mode 100644 docs/general/images/wallet/web/deposit5.png
 create mode 100644 docs/general/images/wallet/web/home.png
 create mode 100644 docs/general/images/wallet/web/import_wallet.png
 create mode 100644 docs/general/images/wallet/web/import_wallet_ledger.png
 create mode 100644 docs/general/images/wallet/web/import_wallet_mnemonic.png
 create mode 100644 docs/general/images/wallet/web/import_wallet_private_key.png
 create mode 100644 docs/general/images/wallet/web/no-profile-dark-theme.png
 create mode 100644 docs/general/images/wallet/web/paratimes.png
 create mode 100644 docs/general/images/wallet/web/settings-my-accounts.png
 create mode 100644 docs/general/images/wallet/web/stake.png
 create mode 100644 docs/general/images/wallet/web/transfer.png
 create mode 100644 docs/general/images/wallet/web/undelegate1.png
 create mode 100644 docs/general/images/wallet/web/undelegate2.png
 create mode 100644 docs/general/images/wallet/web/undelegate3.png
 create mode 100644 docs/general/images/wallet/web/wallet.png
 create mode 100644 docs/general/images/wallet/web/withdraw1.png
 create mode 100644 docs/general/images/wallet/web/withdraw2.png
 create mode 100644 docs/general/images/wallet/web/withdraw3.png
 create mode 100644 docs/general/images/wallet/web/withdraw4.png
 create mode 100644 docs/general/images/wallet/web/withdraw5.png
 delete mode 100644 docs/general/manage-tokens/how-to-transfer-rose-into-paratime.mdx
 delete mode 100644 docs/general/manage-tokens/oasis-wallets/README.mdx
 delete mode 100644 docs/general/manage-tokens/oasis-wallets/browser-extension.md
 create mode 100644 docs/general/manage-tokens/oasis-wallets/browser-extension.mdx
 delete mode 100644 docs/general/manage-tokens/oasis-wallets/web.md
 create mode 100644 docs/general/manage-tokens/oasis-wallets/web.mdx

diff --git a/README.md b/README.md
index 7d286247a1..d1fa074bb9 100644
--- a/README.md
+++ b/README.md
@@ -204,14 +204,18 @@ There are three kinds of image assets used in the docs.
 The following is a consistent case-sensitive collection of Oasis-related terms,
 and their usage including the articles:
 
+- Bech32
 - c10l
   Check out the c10l-hello-world folder for the confidential version of the
   original example.
 - c13y
   EVM with added c13y.
+- CBOR
 - Cipher
 - consensus layer
   The consensus layer makes sure that the ParaTimes tick.
+- Ed25519
+  The consensus layer only supports the Ed25519 signature scheme.
 - Emerald
 - dApp
   Emerald supports writing dApps. DApp is a modern distributed application.
@@ -224,6 +228,8 @@ and their usage including the articles:
 - Oasis CLI
   You can use the Oasis CLI to set up your wallet.
 - Oasis Core
+- Oasis Network
+  The Oasis Network is a proof-of-stake network.
 - OPL
   Oasis Privacy Layer supports privacy of dApps on all EVM chains.
 - ParaTime
@@ -234,11 +240,15 @@ and their usage including the articles:
   Please send 10.00000000 ROSE to the address above.
 - runtime
 - Sapphire
+- secp256k1
+  The Koblitz curve secp256k1 parameters are deterministic.
+- Sr25519
 - TEST
   Please send 10.00000000 TEST to the address above.
 - trusted execution environment
 - validator
 - validator node
+- Wasm
 - Web3 gateway
   We strongly suggest that you set up your own Web3 gateway for your Sapphire
   endpoint.
diff --git a/docs/dapp/cipher/README.mdx b/docs/dapp/cipher/README.mdx
index 561f6c63b6..ba99e32798 100644
--- a/docs/dapp/cipher/README.mdx
+++ b/docs/dapp/cipher/README.mdx
@@ -85,7 +85,7 @@ public list above, open an issue at [github.com/oasisprotocol/docs].
 ## See also
 
 <DocCardList items={[
-    findSidebarItem('/general/manage-tokens/how-to-transfer-rose-into-paratime'),
+    findSidebarItem('/general/manage-tokens/'),
     findSidebarItem('/node/run-your-node/paratime-node'),
     findSidebarItem('/node/run-your-node/paratime-client-node'),
     findSidebarItem('/dapp/emerald/'),
diff --git a/docs/dapp/emerald/README.mdx b/docs/dapp/emerald/README.mdx
index 303b2d4d0a..19033456f8 100644
--- a/docs/dapp/emerald/README.mdx
+++ b/docs/dapp/emerald/README.mdx
@@ -95,7 +95,7 @@ to be added to the public list above, open an issue at
 ## See also'''

        self.assertEqual(compute_relevant_diff(diff2), 1792)

    def test_fetch_changelogs(self):
        item = {'number': 5728}
        item['raw_diff'] = '''
        From 40eae687a39cc16506aad072133cf8b06cd7f4a1 Mon Sep 17 00:00:00 2001
From: Jernej Kos <jernej@kos.mx>
Date: Wed, 26 Jun 2024 22:25:22 +0200
Subject: [PATCH 1/2] runtime: Add SGXConstraints::enclaves method

---
 runtime/src/consensus/registry.rs | 14 +++++++++-----
 1 file changed, 9 insertions(+), 5 deletions(-)

diff --git a/runtime/src/consensus/registry.rs b/runtime/src/consensus/registry.rs
index de80d2a3dd9..a413efc9b99 100644
--- a/runtime/src/consensus/registry.rs
+++ b/runtime/src/consensus/registry.rs
@@ -701,13 +701,17 @@ pub enum SGXConstraints {
 }
 
 impl SGXConstraints {
-    /// Checks whether the given enclave identity is whitelisted.
-    pub fn contains_enclave(&self, eid: &sgx::EnclaveIdentity) -> bool {
-        let enclaves = match self {
+    /// Identities of allowed enclaves.
+    pub fn enclaves(&self) -> &Vec<sgx::EnclaveIdentity> {
+        match self {
             Self::V0 { ref enclaves, .. } => enclaves,
             Self::V1 { ref enclaves, .. } => enclaves,
-        };
-        enclaves.contains(eid)
+        }
+    }
+
+    /// Checks whether the given enclave identity is whitelisted.
+    pub fn contains_enclave(&self, eid: &sgx::EnclaveIdentity) -> bool {
+        self.enclaves().contains(eid)
     }
 
     /// SGX quote policy.

From 32385fdd48d44239ca7edb258152622269d0c4f8 Mon Sep 17 00:00:00 2001
From: Jernej Kos <jernej@kos.mx>
Date: Wed, 26 Jun 2024 22:27:35 +0200
Subject: [PATCH 2/2] runtime: Add VerifiedAttestation with more metadata

Since verified attestations generated from TEE capabilities can include
additional metadata like the enclave's view of consensus layer height at
time of attestation, this allows such data to be used by callers.
---
 .changelog/5728.internal.md        |  5 ++++
 keymanager/src/churp/handler.rs    |  2 +-
 keymanager/src/runtime/secrets.rs  |  2 +-
 runtime/src/consensus/registry.rs  | 48 ++++++++++++++++++++++++------
 runtime/src/enclave_rpc/session.rs | 14 ++++-----
 5 files changed, 53 insertions(+), 18 deletions(-)
 create mode 100644 .changelog/5728.internal.md

diff --git a/.changelog/5728.internal.md b/.changelog/5728.internal.md
new file mode 100644
index 00000000000..2095071b277
--- /dev/null
+++ b/.changelog/5728.internal.md
@@ -0,0 +1,5 @@
+runtime: Add VerifiedAttestation with more metadata
+
+Since verified attestations generated from TEE capabilities can include
+additional metadata like the enclave's view of consensus layer height at
+time of attestation, this allows such data to be used by callers.
diff --git a/keymanager/src/churp/handler.rs b/keymanager/src/churp/handler.rs
index d73bed4b022..a611def8831 100644
--- a/keymanager/src/churp/handler.rs
+++ b/keymanager/src/churp/handler.rs
@@ -1272,7 +1272,7 @@ impl Churp {
     fn remote_enclave(ctx: &RpcContext) -> Result<&EnclaveIdentity> {
         let si = ctx.session_info.as_ref();
         let si = si.ok_or(Error::NotAuthenticated)?;
-        Ok(&si.verified_quote.identity)
+        Ok(&si.verified_attestation.quote.identity)
     }
 
     /// Returns true if key manager policies should be ignored.
diff --git a/keymanager/src/runtime/secrets.rs b/keymanager/src/runtime/secrets.rs
index 10b2b326829..b5210c1836c 100644
--- a/keymanager/src/runtime/secrets.rs
+++ b/keymanager/src/runtime/secrets.rs
@@ -513,7 +513,7 @@ impl Secrets {
     fn authenticate(ctx: &RpcContext) -> Result<&EnclaveIdentity> {
         let si = ctx.session_info.as_ref();
         let si = si.ok_or(KeyManagerError::NotAuthenticated)?;
-        Ok(&si.verified_quote.identity)
+        Ok(&si.verified_attestation.quote.identity)
     }
 
     /// Fetch current epoch from the consensus layer.
diff --git a/runtime/src/consensus/registry.rs b/runtime/src/consensus/registry.rs
index a413efc9b99..939939a2bc8 100644
--- a/runtime/src/consensus/registry.rs
+++ b/runtime/src/consensus/registry.rs
@@ -161,7 +161,7 @@ impl CapabilityTEE {
         &self,
         policy: &sgx::QuotePolicy,
         node_id: &signature::PublicKey,
-    ) -> anyhow::Result<sgx::VerifiedQuote> {
+    ) -> anyhow::Result<VerifiedAttestation> {
         match self.hardware {
             TEEHardware::TEEHardwareInvalid => bail!("invalid TEE hardware"),
             TEEHardware::TEEHardwareIntelSGX => {
@@ -216,12 +216,12 @@ impl EndorsedCapabilityTEE {
         self.verify_endorsement()?;
 
         // Verify TEE capability.
-        let verified_quote = self
+        let verified_attestation = self
             .capability_tee
             .verify(policy, &self.node_endorsement.public_key)?;
 
         Ok(VerifiedEndorsedCapabilityTEE {
-            verified_quote,
+            verified_attestation,
             node_id: Some(self.node_endorsement.public_key),
         })
     }
@@ -230,16 +230,25 @@ impl EndorsedCapabilityTEE {
 /// A verified endorsed CapabilityTEE structure.
 #[derive(Clone, Debug, Default)]
 pub struct VerifiedEndorsedCapabilityTEE {
-    /// Verified TEE quote.
-    pub verified_quote: sgx::VerifiedQuote,
+    /// Verified TEE remote attestation.
+    pub verified_attestation: VerifiedAttestation,
     /// Optional identifier of the node that endorsed the TEE capability.
     pub node_id: Option<signature::PublicKey>,
 }
 
+impl From<VerifiedAttestation> for VerifiedEndorsedCapabilityTEE {
+    fn from(verified_attestation: VerifiedAttestation) -> Self {
+        Self {
+            verified_attestation,
+            node_id: None,
+        }
+    }
+}
+
 impl From<sgx::VerifiedQuote> for VerifiedEndorsedCapabilityTEE {
     fn from(verified_quote: sgx::VerifiedQuote) -> Self {
         Self {
-            verified_quote,
+            verified_attestation: verified_quote.into(),
             node_id: None,
         }
     }
@@ -734,6 +743,24 @@ impl SGXConstraints {
     }
 }
 
+/// Verified remote attestation.
+#[derive(Clone, Debug, Default)]
+pub struct VerifiedAttestation {
+    /// Verified enclave quote.
+    pub quote: sgx::VerifiedQuote,
+    /// Enclave's view of the consensus layer height at the time of attestation.
+    pub height: Option<u64>,
+}
+
+impl From<sgx::VerifiedQuote> for VerifiedAttestation {
+    fn from(quote: sgx::VerifiedQuote) -> Self {
+        Self {
+            quote,
+            height: None,
+        }
+    }
+}
+
 /// Intel SGX remote attestation.
 #[derive(Clone, Debug, cbor::Encode, cbor::Decode)]
 #[cbor(tag = "v")]
@@ -787,7 +814,7 @@ impl SGXAttestation {
         node_id: &signature::PublicKey,
         rak: &signature::PublicKey,
         rek: &x25519::PublicKey,
-    ) -> anyhow::Result<sgx::VerifiedQuote> {
+    ) -> anyhow::Result<VerifiedAttestation> {
         // Verify the quote.
         let verified_quote = self.quote().verify(policy)?;
 
@@ -801,11 +828,14 @@ impl SGXAttestation {
             } => {
                 let h = Self::hash(&verified_quote.report_data, node_id, *height, rek);
                 signature.verify(rak, ATTESTATION_SIGNATURE_CONTEXT, &h)?;
+
+                Ok(VerifiedAttestation {
+                    quote: verified_quote,
+                    height: Some(*height),
+                })
             }
             _ => bail!("V0 attestation not supported"),
         }
-
-        Ok(verified_quote)
     }
 }
 
diff --git a/runtime/src/enclave_rpc/session.rs b/runtime/src/enclave_rpc/session.rs
index 27cf5a14a33..6f406a2215c 100644
--- a/runtime/src/enclave_rpc/session.rs
+++ b/runtime/src/enclave_rpc/session.rs
@@ -9,10 +9,10 @@ use crate::{
     common::{
         crypto::signature::{self, PublicKey, Signature, Signer},
         namespace::Namespace,
-        sgx::{ias, EnclaveIdentity, Quote, QuotePolicy, VerifiedQuote},
+        sgx::{ias, EnclaveIdentity, Quote, QuotePolicy},
     },
     consensus::{
-        registry::{EndorsedCapabilityTEE, VerifiedEndorsedCapabilityTEE},
+        registry::{EndorsedCapabilityTEE, VerifiedAttestation, VerifiedEndorsedCapabilityTEE},
         state::registry::ImmutableState as RegistryState,
         verifier::Verifier,
     },
@@ -53,8 +53,8 @@ enum SessionError {
 pub struct SessionInfo {
     /// RAK binding.
     pub rak_binding: RAKBinding,
-    /// Verified TEE quote.
-    pub verified_quote: VerifiedQuote,
+    /// Verified TEE remote attestation.
+    pub verified_attestation: VerifiedAttestation,
     /// Identifier of the node that endorsed the TEE.
     pub endorsed_by: Option<PublicKey>,
 }
@@ -281,7 +281,7 @@ impl Session {
 
         Ok(Some(Arc::new(SessionInfo {
             rak_binding,
-            verified_quote: vect.verified_quote,
+            verified_attestation: vect.verified_attestation,
             endorsed_by: vect.node_id,
         })))
     }
@@ -428,11 +428,11 @@ impl RAKBinding {
 
         // Ensure that the report data includes the hash of the node's RAK.
         // NOTE: For V2 this check is part of verify_inner so it is not really needed.
-        Identity::verify_binding(&vect.verified_quote, &self.rak_pub())?;
+        Identity::verify_binding(&vect.verified_attestation.quote, &self.rak_pub())?;
 
         // Verify MRENCLAVE/MRSIGNER.
         if let Some(ref remote_enclaves) = remote_enclaves {
-            if !remote_enclaves.contains(&vect.verified_quote.identity) {
+            if !remote_enclaves.contains(&vect.verified_attestation.quote.identity) {
                 return Err(SessionError::MismatchedEnclaveIdentity.into());
             }
         }
'''
        fetch_changelogs([item])
        self.assertEqual(item['changelog'],'''runtime: Add VerifiedAttestation with more metadata<br/> Since verified attestations generated from TEE capabilities can include additional metadata like the enclave's view of consensus layer height at time of attestation, this allows such data to be used by callers. ''')

        item = {'number': 709}
        item['raw_diff'] = '''
        From b368055f1d254221d5eb5bd79148a43947fd0af8 Mon Sep 17 00:00:00 2001
From: ptrus <peter@u-s.si>
Date: Mon, 17 Jun 2024 15:06:51 +0200
Subject: [PATCH] api/epochs: Skip 'end_height' for latest epoch

---
 .changelog/709.bugfix.md                        |  1 +
 storage/client/client.go                        |  5 ++++-
 storage/client/queries/queries.go               | 10 +++-------
 tests/e2e_regression/damask/expected/epoch.body |  1 -
 4 files changed, 8 insertions(+), 9 deletions(-)
 create mode 100644 .changelog/709.bugfix.md

diff --git a/.changelog/709.bugfix.md b/.changelog/709.bugfix.md
new file mode 100644
index 000000000..2ba04f568
--- /dev/null
+++ b/.changelog/709.bugfix.md
@@ -0,0 +1 @@
+`/api/consensus/<epoch>`: Do not return end_height for currently active epoch
diff --git a/storage/client/client.go b/storage/client/client.go
index 5211734b4..7a8ad37e2 100644
--- a/storage/client/client.go
+++ b/storage/client/client.go
@@ -1004,6 +1004,7 @@ func (c *StorageClient) Epochs(ctx context.Context, p apiTypes.GetConsensusEpoch
 	res, err := c.withTotalCount(
 		ctx,
 		queries.Epochs,
+		nil,
 		p.Limit,
 		p.Offset,
 	)
@@ -1033,8 +1034,10 @@ func (c *StorageClient) Epoch(ctx context.Context, epoch int64) (*Epoch, error)
 	var e Epoch
 	if err := c.db.QueryRow(
 		ctx,
-		queries.Epoch,
+		queries.Epochs,
 		epoch,
+		1,
+		0,
 	).Scan(&e.ID, &e.StartHeight, &e.EndHeight); err != nil {
 		return nil, wrapError(err)
 	}
diff --git a/storage/client/queries/queries.go b/storage/client/queries/queries.go
index c25beb81c..ac145362c 100644
--- a/storage/client/queries/queries.go
+++ b/storage/client/queries/queries.go
@@ -252,14 +252,10 @@ const (
 		SELECT id, start_height,
 			(CASE id WHEN (SELECT max(id) FROM chain.epochs) THEN NULL ELSE end_height END) AS end_height
 			FROM chain.epochs
+		WHERE ($1::bigint IS NULL OR id = $1::bigint)
 		ORDER BY id DESC
-		LIMIT $1::bigint
-		OFFSET $2::bigint`
-
-	Epoch = `
-		SELECT id, start_height, end_height
-			FROM chain.epochs
-			WHERE id = $1::bigint`
+		LIMIT $2::bigint
+		OFFSET $3::bigint`
 
 	Proposals = `
 		SELECT id, submitter, state, deposit, handler, cp_target_version, rhp_target_version, rcp_target_version,
diff --git a/tests/e2e_regression/damask/expected/epoch.body b/tests/e2e_regression/damask/expected/epoch.body
index 7f993d88b..ec13f720a 100644
--- a/tests/e2e_regression/damask/expected/epoch.body
+++ b/tests/e2e_regression/damask/expected/epoch.body
@@ -1,5 +1,4 @@
 {
-  "end_height": 8049955,
   "id": 13403,
   "start_height": 8049556
 }
'''

        fetch_changelogs([item])
        self.assertEqual(item['changelog'],
                         '''`/api/consensus/<epoch>`: Do not return end_height for currently active epoch ''')


if __name__ == '__main__':
    unittest.main()