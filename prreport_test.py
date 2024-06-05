import unittest

from prreport import *

class TestPRReport(unittest.TestCase):

    def test_format_body(self):
        self.assertEqual(format_body('hello world\r\nnew line'), 'hello world<br/>\nnew line')


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


if __name__ == '__main__':
    unittest.main()