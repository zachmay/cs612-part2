//===- Hello.cpp - Example code from "Writing an LLVM Pass" ---------------===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//
//
// This file implements two versions of the LLVM "Hello World" pass described
// in docs/WritingAnLLVMPass.html
//
//===----------------------------------------------------------------------===//

#include "llvm/ADT/Statistic.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/Instruction.h"
#include "llvm/IR/DebugLoc.h"
#include "llvm/IR/DebugInfoMetadata.h"
#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"
using namespace llvm;

#define DEBUG_TYPE "cdg"

STATISTIC(CdgCounter, "Counts number of functions greeted");

namespace {
  // Zach - The first implementation, without getAnalysisUsage.
  struct CDG : public ModulePass {
    static char ID; // Pass identification, replacement for typeid
    CDG() : ModulePass(ID) {}

    bool runOnModule(Module &module) override {
      ++CdgCounter;
      for ( auto &f : module.getFunctionList() )
      {
          for ( auto &bb : f.getBasicBlockList() )
          {
              unsigned firstLine = -1;
              unsigned firstCol = -1;
              
              for ( auto& instr : bb )
              {
                  if ( DILocation *loc = instr.getDebugLoc() )
                  {
                      firstLine = loc->getLine();
                      firstCol = loc->getColumn();
                      break;
                  }
              }
              
              errs()
                << module.getModuleIdentifier()
                << "_"
                << f.getName()
                << "_"
                << bb.getName()
                << ":"
                << firstLine
                << ":"
                << firstCol
                << '\n';
              
          }
      }
      return false;
    }
  };
}

char CDG::ID = 99;
static RegisterPass<CDG> X("cdg", "Compute CDG");
